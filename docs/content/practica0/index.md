+++
date = '2026-02-14T23:44:47-06:00'
draft = false
title = 'Practica0: Manejo de repositorios'
+++

## Descripción de la práctica

Esta practica consistio en aprender a crear una pagina web, primero utilizamos markdown para creacion de documentos,luego usamos git para gestionar los cambios hechos en el proyecto y utilizamos github para guardar el repositorio en la nube.Despues creamos un sitio web usnado HUGO y tambien utilizamos github actions para la publicacion de nuestra pagina, gracias a este, cada que subiamos algun cambio al repositorio, el sitio se actualizaba automaticamente en github pages.

## Desarrollo de la práctica
Markdown es un lenguaje  de marcado ligero que permite dar formato a textos,lo tulizamos haciendo nuestro index.md para nuestra practica0,la ventaja de markdown es que solo debes usar simbolos simples.Utilizamos tambien comandos de git como git push ,git add. y git commit ,ademas utilizamos github y un repositorio para guardar conectar nuestro repositorio local al remoto que eta en github, tambien al estar en github,configuramos github actions para que automaticamente se contruyera el sitio y se publicara, tambien si quieriamos actualizar algo en esa pagina,utilizamos el ya mencionado git push.

### Primera sesión – Markdown

El formato markdown es un lenguaje de marcado simple que nos permite dar  forma a los textos sin necesidad de utilizar codigo o sabe algo de programacion.
Para hacer un archivo markdown, se escribe el .md despues del nombre de tu archivo.
Markdown puede ser utilizado en editores de texto como:Vs code,Bloc de notas, github y hugo.
La sintaxis es:
Título principal seguido de un asterisco
Subtítulo seguido de un asterisco
Para un texto en negrita se escribe pone por ejemplo **negritas**, texto en cursiva es *cursiva*
Para una lista enumerdad haces por ejemplo:
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
git commit -m "mensaje deseado"

creamos nuestro repositorio en github y copiamos el url del repositorio
usamos luego git remote add origin (url del repositorio)
git push -u origin master
Se revisa el repositorio online en github para ver que todo haya salido bien.

### Tercera sesión – Hugo y GitHub Actions

Hugo es un

## Conclusiones

Aquí escribes tus conclusiones...
