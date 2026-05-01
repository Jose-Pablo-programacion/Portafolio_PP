+++
date = '2026-02-14T23:50:36-06:00'
draft = false
title = 'Practica3: El paradigma funcional'
+++


Instalación de entorno
Para instalar el entorno de desarrollo de Haskell se utilizó GHCup, la herramienta oficial recomendada en la página de descargas de Haskell (haskell.org/downloads). 

Se abrio powershell y se ejecuto = Set-ExecutionPolicy Bypass -Scope Process -Force;[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; try { & ([ScriptBlock]::Create((Invoke-WebRequest https://www.haskell.org/ghcup/sh/bootstrap-haskell.ps1 -UseBasicParsing))) -Interactive -DisableCurl } catch { Write-Error $_ } 

se realizaron las siguiente acciones:
1.Se le da enter



![alt text](image.png)



2.Se le da enter




![alt text](image-1.png)



3.Se escribe Y y se le da enter



![alt text](image-2.png)





4.Se escribe Y y se le da enter



![alt text](image-3.png)




5.Se escribe Y y se le da enter



![alt text](image-4.png)



La instalacion se atoro a la mitad y se tuvo que cancelar usando ctrl + c pero se alcanzo a instalar GHcup y MSys2


En el segundo intento se continuo haciendo esto:
1.Se escribe C y se le da enter


![alt text](image-5.png)



Se volvió a ejecutar el comando, el instalador detectó GHCup y MSys2 ya instalados y continuó desde donde se había quedado. Se escribio Y a las preguntas de instalar HLS, Stack y crear accesos directos en el escritorio y se le dio enter

2.Se continuo con la instalacion




![alt text](image-6.png)



3.



![alt text](image-7.png)




4.



![alt text](image-8.png)





5.Se terminó de instalar todo correctamente.



![alt text](image-9.png)





6.Se cierra esa pestaña y tambien la de powershell, se vuelve a abrir powershell y para confirmar que todo se instaló correctamente, se ejecutan los comandos de las versiones de ghc,stack y cabal.




![alt text](image-10.png)





Para verificar que funcione bien el entorno, se ejecuta en powershell el comando ghci




![alt text](image-11.png)




A continuación se ejecutan nuestras primeras lineas de código


![alt text](image-12.png)



![alt text](image-13.png)


![alt text](image-14.png)



A continuación nos vamos a Vs code y creamos un archivo con extensión .hs y ejecutamos el siguiente código que nos otorga la guía oficial.





![alt text](image-15.png)





Ahora compilamos y ejecutamos el codigo en powershell



![alt text](image-16.png)



Ahora se instala la app TODO



![alt text](image-17.png)



Ya nos aparece en vscode también


![alt text](image-18.png)



Ahora navegamos a la carpeta de la app TODO 


![alt text](image-19.png)



Ahora compilamos la app con stack, se ejecuta stack build





![alt text](image-20.png)





Ahora creamos un archivo.env para correr el stack y tambien creamos la variable WEBSITE en el archivo.env



![alt text](image-21.png)



![alt text](image-22.png)




![alt text](image-23.png)



Como podemos ver la aplicación tiene diferentes comandos que son:
1.+ para agregar nuevas tareas
2.- para eliminar una tarea por su número
3.l para listar las tareas
4.s para mostrar el detalle de una tarea por su número
5.e para editar tareas
6.r para invertir el orden de la lista de tareas
7.c para borrar todas las tareas
8.q para salir de la aplicación

ahora escribimos por ejemplo +aprender Haskell


![alt text](image-24.png)




Ahora escribimos l para listar y ver que quedó guardada.



![alt text](image-25.png)



podemos poner otra mas


![alt text](image-26.png)


y luego escribir nuevamente l



![alt text](image-27.png)




Conclusión= En esta práctica se instaló se configuró el entorno de Haskell usando GHcup, se usó stack y la herramienta de empaquetado Cabal.Se ejecuto un codigo básico en Haskell y finalmente se ejecuto la aplicacion TODO escrita en Haskell donde se nos permite gestionar tareas desde la terminal de comandos mediante comandos. 