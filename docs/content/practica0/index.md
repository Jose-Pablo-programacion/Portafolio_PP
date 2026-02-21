+++
date = '2026-02-14T23:44:47-06:00'
draft = false
title = 'Practica0: Manejo de repositorios'
+++

## Descripción de la práctica

Esta practica consistio en aprender a crear una pagina web, primero utilizamos markdown para creacion de documentos,luego usamos git para gestionar los cambios hechos en el proyecto y utilizamos github para guardar el repositorio en la nube.Despues creamos un sitio web usando HUGO y tambien utilizamos github actions para la publicacion de nuestra pagina, gracias a este, cada que subiamos algun cambio al repositorio, el sitio se actualizaba automaticamente en github pages.

## Desarrollo de la práctica
Markdown es un lenguaje  de marcado ligero que permite dar formato a textos,lo utilizamos haciendo nuestro index.md para nuestra practica0,la ventaja de markdown es que solo debes usar simbolos simples.Utilizamos tambien comandos de git como git push ,git add. y git commit ,ademas utilizamos github y un repositorio para guardar conectar nuestro repositorio local al remoto que esta en github, tambien al estar en github,configuramos github actions para que automaticamente se contruyera el sitio y se publicara, tambien si quieriamos actualizar algo en esa pagina,utilizamos el ya mencionado git push.

### Primera sesión – Markdown

El formato markdown es un lenguaje de marcado simple que nos permite dar forma a los textos sin necesidad de utilizar codigo o sabe algo de programacion.
Para hacer un archivo markdown, se escribe el .md despues del nombre de tu archivo.
Markdown puede ser utilizado en editores de texto como:Vs code,Bloc de notas, github y hugo.
La sintaxis es:
Título principal seguido de un asterisco.
Subtítulo seguido de un asterisco.
Para un texto en negrita se escribe pone por ejemplo **negritas**, texto en cursiva es *cursiva*
Para una lista enumerada haces por ejemplo:
1. Primer punto
2. Segundo punto
3. Tercer punto

Para imagenes puede hacer
![Texto alternativo](imagen.jpg)
La linea separadora se hace con ---

### Segunda sesión – Git y GitHub

Github:Github es una gran comunidad de codigo abierto.Al explorar Github puedes encontrar repositorios,temas,codigos,usuarios y organizaciones.

Git:Git es un sistema de control de versiones distribuido,gratuito y de codigo abierto diseñado para gestionar el historial de cambios  en archivos y codigo fuente de forma rapida y eficiente.

Primero creamos el proyecto en local
usamos git init
git add .
git commit -m "se hizo el repositorio local"

creamos nuestro repositorio en github y copiamos el url del repositorio
usamos luego git remote add origin (url del repositorio)
git push -u origin master
Se revisa el repositorio online en github para ver que todo haya salido bien.

### Tercera sesión – Hugo y GitHub Actions

Hugo es uno de los generadores de sitios web estáticos de código abierto más populares. Con su increíble velocidad y flexibilidad, Hugo hace que crear sitios web vuelva a ser divertido.
Github actions es una plataforma de automatizacion de flujos de trabajo integrada a github que permite compilar,probar y desplegar codigo automaticamente.
Para crear el proyecto hugo hacemos:
1. hugo new site docs
2. cd docs
3. hugo new practica0/index.md
4. Cambiamos draft a false
5. hugo server
para subirlo en github
1. git add
2. git commit -m "crear sitio hugo"
3. push

Para configurar github actions para publicar nuestro sitio  en github pages,hacemos:
1. mkdir -p .github/workflows
2. touch .github/workflows/hugo.yaml
3. Ajustamos a la rama correcta osea el branch master
Subimos el archivo con
1. git add
2. git commit -m "agregar workflow de github pages"
3. push

## Conclusiones
    Es esta practica aprendi sobre como crear sitios utilizando hugo y tambien archivos markdown para generar el contenido de una forma sencilla.Tambien aprendi a como hacer un repositorio local y como convertirlo en uno remoto utilizando git y github, tambien aprendi a usar github pages para publicar una pagina en internet.Fue sorprendente ver que no es necesario saber mucha programacion para poder utilizar markdown gracias a su simplicidad.


## Enlaces
https://github.com/Jose-Pablo-programacion/Portafolio_PP#

https://jose-pablo-programacion.github.io/Portafolio_PP/