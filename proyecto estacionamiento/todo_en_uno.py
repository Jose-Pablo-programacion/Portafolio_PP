import sys
from datetime import datetime, timedelta
from flask import Flask, render_template_string, request, redirect, url_for, flash

# ══════════════════════════════════════════════════════════════════════════════
# 1. MODELOS DE DATOS (POO: HERENCIA Y POLIMORFISMO)
# ══════════════════════════════════════════════════════════════════════════════

class Vehicle:
    def __init__(self, plate):
        if not plate: raise ValueError("La placa es obligatoria.")
        self._plate = plate
    def get_plate(self): return self._plate

class Car(Vehicle):
    def __str__(self): return f"Auto [{self.get_plate()}]"

class Motorcycle(Vehicle):
    def __str__(self): return f"Moto [{self.get_plate()}]"

class RatePolicy:
    def calculate(self, entry_time, exit_time, vehicle): pass

class HourlyRatePolicy(RatePolicy):
    def calculate(self, entry_time, exit_time, vehicle):
        duration = (exit_time - entry_time).total_seconds() / 3600
        rate = 10 if isinstance(vehicle, Car) else 5
        return round(max(1, duration) * rate, 2)

class FlatRatePolicy(RatePolicy):
    def calculate(self, entry_time, exit_time, vehicle):
        return 20.0 

class ParkingTicket:
    def __init__(self, ticket_id, vehicle, spot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()

class SpotType:
    CAR = "Car"
    MOTO = "Motorcycle"
    ANY = "Any"

class ParkingSpot:
    def __init__(self, spot_id, allowed_type):
        self.spot_id = spot_id
        self.allowed = allowed_type
        self.occupied = False
        self.vehicle = None
    def assign(self, vehicle):
        self.occupied = True
        self.vehicle = vehicle
    def release(self):
        self.occupied = False
        self.vehicle = None

class ParkingLot:
    def __init__(self):
        self._spots = [ParkingSpot(f"A{i}", SpotType.CAR) for i in range(1, 6)] + \
                      [ParkingSpot(f"M{i}", SpotType.MOTO) for i in range(1, 4)] + \
                      [ParkingSpot(f"G{i}", SpotType.ANY) for i in range(1, 3)]
        self._tickets = {}
        self._next_id = 1
        self._policy = HourlyRatePolicy()

    def enter(self, vehicle):
        target = SpotType.CAR if isinstance(vehicle, Car) else SpotType.MOTO
        spot = next((s for s in self._spots if not s.occupied and (s.allowed == target or s.allowed == SpotType.ANY)), None)
        if not spot: raise Exception("No hay lugar disponible.")
        t = ParkingTicket(self._next_id, vehicle, spot)
        spot.assign(vehicle)
        self._tickets[self._next_id] = t
        self._next_id += 1
        return t

    def exit(self, tid, manual_now=None):
        t = self._tickets.pop(tid, None)
        if not t: raise Exception("Ticket no encontrado.")
        cost = self._policy.calculate(t.entry_time, manual_now or datetime.now(), t.vehicle)
        t.spot.release()
        return cost

    def get_spots(self): return self._spots
    def get_active_tickets(self): return list(self._tickets.values())

# ══════════════════════════════════════════════════════════════════════════════
# 2. INTERFAZ WEB (FLASK)
# ══════════════════════════════════════════════════════════════════════════════

TEMPLATES = {
    'base.html': '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ title }}</title>
            <style>
                body { font-family: sans-serif; background: #f4f7f6; padding: 20px; }
                .container { max-width: 850px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                h1 { color: #1F4E79; text-align: center; }
                nav { text-align: center; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #eee; }
                nav a { margin: 0 12px; text-decoration: none; color: #2E74B5; font-weight: bold; }
                .box { border: 1px solid #ddd; padding: 15px; border-radius: 5px; }
                table { width: 100%; border-collapse: collapse; margin-top: 10px; }
                th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
                th { background: #1F4E79; color: white; }
                .btn { background: #2E74B5; color: white; padding: 10px; border: none; width: 100%; cursor: pointer; border-radius: 4px; font-weight: bold; }
                .alert { padding: 12px; margin-bottom: 15px; border-radius: 4px; background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🏎 Simulador de Estacionamiento</h1>
                <nav>
                    <a href="/">Dashboard</a>
                    <a href="/entry">Registrar Entrada</a>
                    <a href="/exit">Registrar Salida</a>
                    <a href="/policy">Configuración</a>
                </nav>
                {% with msgs = get_flashed_messages() %}{% for m in msgs %}<div class="alert">{{m}}</div>{% endfor %}{% endwith %}
                {% block content %}{% endblock %}
            </div>
        </body>
        </html>
    ''',
    'dashboard.html': '''
        {% extends "base.html" %}
        {% block content %}
        <div class="box">
            <h3>Estado de los Spots</h3>
            <table>
                <tr><th>ID</th><th>Tipo Permitido</th><th>Estado</th></tr>
                {% for s in spots %}
                <tr><td>{{s.spot_id}}</td><td>{{s.allowed}}</td><td style="color:{{'#dc3545' if s.occupied else '#28a745'}}; font-weight:bold;">{{'OCUPADO' if s.occupied else 'libre'}}</td></tr>
                {% endfor %}
            </table>
            <br>
            <h3>Tickets Activos</h3>
            {% if tickets %}
            <table>
                <tr><th>#</th><th>Placa</th><th>Entrada</th></tr>
                {% for t in tickets %}
                <tr><td>{{t.ticket_id}}</td><td>{{t.vehicle.get_plate()}}</td><td>{{t.entry_time.strftime('%H:%M:%S')}}</td></tr>
                {% endfor %}
            </table>
            {% else %}<p>No hay vehículos registrados.</p>{% endif %}
        </div>
        {% endblock %}
    ''',
    'entry.html': '''
        {% extends "base.html" %}
        {% block content %}
        <div class="box">
            <h3>Entrada de Vehículo</h3>
            <form method="POST">
                <label>Placa:</label><br>
                <input type="text" name="plate" required style="width:97%; padding:8px; margin:10px 0;"><br>
                <label>Tipo:</label><br>
                <select name="type" style="width:100%; padding:8px; margin-bottom:20px;">
                    <option value="car">Carro</option>
                    <option value="moto">Motocicleta</option>
                </select>
                <button class="btn">Registrar Entrada</button>
            </form>
        </div>
        {% endblock %}
    ''',
    'exit.html': '''
        {% extends "base.html" %}
        {% block content %}
        <div class="box">
            <h3>Salida de Vehículo</h3>
            <form method="POST">
                <label>ID de Ticket:</label><br>
                <input type="number" name="tid" required style="width:97%; padding:8px; margin:10px 0;"><br>
                <label>Horas de Simulación (Opcional):</label><br>
                <input type="number" step="0.1" name="hours" placeholder="0 para tiempo real" style="width:97%; padding:8px; margin-bottom:20px;"><br>
                <button class="btn">Procesar Pago y Salida</button>
            </form>
        </div>
        {% endblock %}
    ''',
    'policy.html': '''
        {% extends "base.html" %}
        {% block content %}
        <div class="box">
            <h3>Configuración de Cobro</h3>
            <form method="POST">
                <p>Elija el método de cobro polimórfico:</p>
                <select name="policy" style="width:100%; padding:10px; margin-bottom:20px;">
                    <option value="hourly">Tarifa por Hora (C:$10 / M:$5)</option>
                    <option value="flat">Tarifa Plana ($20 Fijo)</option>
                </select>
                <button class="btn">Actualizar Sistema</button>
            </form>
        </div>
        {% endblock %}
    '''
}

def setup_flask(lot):
    app = Flask(__name__)
    app.secret_key = "universidad"

    @app.route('/')
    def dashboard():
        return render_template_string(TEMPLATES['dashboard.html'], title="Dashboard", 
                                     spots=lot.get_spots(), tickets=lot.get_active_tickets())

    @app.route('/entry', methods=['GET', 'POST'])
    def entry():
        if request.method == 'POST':
            try:
                v = Car(request.form['plate']) if request.form['type'] == 'car' else Motorcycle(request.form['plate'])
                t = lot.enter(v)
                flash(f"Registro exitoso. Ticket #{t.ticket_id}")
                return redirect('/')
            except Exception as e: flash(str(e))
        return render_template_string(TEMPLATES['entry.html'], title="Entrada")

    @app.route('/exit', methods=['GET', 'POST'])
    def exit():
        if request.method == 'POST':
            try:
                h = float(request.form.get('hours') or 0)
                cost = lot.exit(int(request.form['tid']), datetime.now() + timedelta(hours=h) if h > 0 else None)
                flash(f"Salida confirmada. Total: ${cost:.2f}")
                return redirect('/')
            except Exception as e: flash(str(e))
        return render_template_string(TEMPLATES['exit.html'], title="Salida")

    @app.route('/policy', methods=['GET', 'POST'])
    def policy():
        if request.method == 'POST':
            lot._policy = FlatRatePolicy() if request.form['policy'] == 'flat' else HourlyRatePolicy()
            flash("Sistema actualizado con la nueva política.")
            return redirect('/')
        return render_template_string(TEMPLATES['policy.html'], title="Configuración")

    return app

# ══════════════════════════════════════════════════════════════════════════════
# 3. INTERFAZ DE CONSOLA (CLI - 6 OPCIONES EXACTAS)
# ══════════════════════════════════════════════════════════════════════════════

def cli_menu(lot):
    while True:
        print("\n" + "="*45)
        print("   SIMULADOR DE ESTACIONAMIENTO - MENÚ")
        print("="*45)
        print("  1. Registrar entrada")
        print("  2. Registrar salida")
        print("  3. Ver ocupación")
        print("  4. Ver tickets activos")
        print("  5. Cambiar política de cobro")
        print("  6. Salir")
        print("="*45)
        
        opt = input("Seleccione una opción: ").strip()
        
        if opt == "1":
            p = input("Placa: ").upper()
            t = input("Tipo (1-Car, 2-Moto): ")
            try:
                v = Car(p) if t == "1" else Motorcycle(p)
                tk = lot.enter(v)
                print(f"\n✔ Ticket #{tk.ticket_id} creado en spot {tk.spot.spot_id}")
            except Exception as e: print(f"\n✘ Error: {e}")
        elif opt == "2":
            try:
                tid = int(input("ID Ticket: "))
                h = float(input("Simular horas: ") or 0)
                cost = lot.exit(tid, datetime.now() + timedelta(hours=h) if h > 0 else None)
                print(f"\n✔ Cobro realizado: ${cost:.2f}")
            except Exception as e: print(f"\n✘ Error: {e}")
        elif opt == "3":
            print("\nEstado de Cajones:")
            for s in lot.get_spots():
                st = "OCUPADO" if s.occupied else "libre"
                print(f"  {s.spot_id:3} | {s.allowed:10} | {st}")
        elif opt == "4":
            tks = lot.get_active_tickets()
            print(f"\nTickets en curso ({len(tks)}):")
            for t in tks:
                print(f"  #{t.ticket_id} | {t.vehicle.get_plate()} | Entró: {t.entry_time.strftime('%H:%M')}")
        elif opt == "5":
            print("\n1. Cobro por Hora | 2. Tarifa Plana ($20)")
            p = input("Opción: ")
            lot._policy = FlatRatePolicy() if p == "2" else HourlyRatePolicy()
            print("✔ Política cambiada exitosamente.")
        elif opt == "6":
            print("\nSaliendo del programa...\n")
            break

# ══════════════════════════════════════════════════════════════════════════════
# 4. PUNTO DE ARRANQUE
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parking = ParkingLot()
    if len(sys.argv) > 1 and sys.argv[1] == "web":
        setup_flask(parking).run(debug=True)
    else:
        cli_menu(parking)