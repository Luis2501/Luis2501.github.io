---
layout: post
title: 'Documentos científicos con $\LaTeX{}$ (SPA)'
date: 2021-08-13 10:30:10
description: Introducción e instalación de LaTeX
tags:
  - latex
categories: tutorial
---

$\LaTeX{}$ (escrito como LaTeX en texto sin formato) es un software de composición de textos, orientado especialmente a la creación de documentos científicos (libros, artículos, tesis, etc) que contienen expresiones matemáticas.

Básicamente se puede decir que $\LaTeX{}$ es como Microsoft Word pero especializado para científicos. Para visualizar un poco mejor el poder de $\LaTeX{}$ te dejo el siguiente documento de ejemplo: 
<!-- [Documento de ejemplo](http://Luis2501.github.io/files/Modelación_simulación_de_señales_neuronales_con_circuitos_RC.pdf)-->

# Instalación de $\LaTeX$

Para poder instalar $\LaTeX$ se requiere de una distribución de TeX, dependiendo el sistema operativo de tu computadora existen diferentes distribuciones. Yo te dare los que pienso son mejor dependiendo el sistema operativo.

_______________________

## Windows

La distribución de Tex que instalaremos es MikTex. Las características más apreciables de MiKTeX son su habilidad de actualizarse por sí mismo (descargando nuevas versiones de componentes y paquetes instalados previamente) y su fácil proceso de instalación. Para instalarlo debemos ir al siguiente enlace: [https://miktex.org/download](https://miktex.org/download)

Al final de la página nos aparecera algo como lo siguiente

<img src="../../../../images/MikTex.png" alt="Imagen">

De manera inmediata podemos descargar el instalador. Sin embargo, si tu computadora no es de 64-bits, deberas dar click en *All downloads* y descargar el correspondiente. 

<img src="../../../../images/MikTex_2.png" alt="Imagen 2">

Descargado el instalador, ejecútalo. El proceso es muy sencillo, sigue los pasos que te indican (aceptar licencia y carpeta de destino) y en unos minutos tendrás MiKTeX instalado.

Una vez instalado MiKTeX es hora debemos escojer un editor de textos para $\LaTeX{}$; personalmente prefiero **TexMaker**. Para instalar Texmaker entra en la página oficial: [xm1math.net/texmaker](xm1math.net/texmaker) 

Damos click en *Download*. 

<img src="../../../../images/TexMaker.png" alt="Imagen 3">

A continuación elige el sistema operativo, en este caso Windows, y descarga el instalador. 

<img src="../../../../images/TexMaker_2.png" alt="Imagen 4">

Ahora ejecútalo, sigue los pasos y en pocos segundos lo tendrás instalado.


___________________________

## Linux

<p style="text-align: justify">
Debo aclarar que la siguiente instalación es mediante Debian/Ubuntu. Antes de comenzar a instalar, debe abrir una terminal y ejecutar los siguiente comandos:
</p>

``` console
sudo apt-get update
sudo apt upgrade
```

Ahora, lo primero es instalar TeX Live. TeX Live es una distribución de LaTeX y es la distribución por defecto para varias distribuciones Linux tales como Debian y Ubuntu. Para instalarlo entra en la misma terminal ejecutamos el comando:

``` console
sudo apt-get install texlive-full
```

Ya que hemos instalado Tex Live, requerimos de un editor de texto específico $\LaTeX{}$. El que más me gusta es Texmaker, para instalarlo ejecutamos en la terminal:


``` console
sudo apt-get install texmaker
```

Esto nos indica que Anaconda sea ha instaldo. La palabra `(base)` antes del prompt indica que nos encontramos en el entorno base de Anaconda. Quizás después hable un poco acerca de los entornos virtuales de Anaconda.

________________________

## Creando el primer documento

Para comprobar que todo funciona correctamente, lo mejor es probar haciendo un primer documento. Para ello abrimos Texmaker y una vez dentro nos aparecera algo como lo siguiente

<img src="../../../../images/Latex.png" alt="Imagen 5">

Creamos documento nuevo dando click en el botón que se encuentra en la esquina superior izquierda, por debajo de `Archivo`. Guardamos el documento con el nombre que deseas, dando click en el tercer botón en la misma fila. Yo lo guardare como `Primer_documento` .

Después, escribimos el siguiente código:

``` latex
\documentclass[a4paper,10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[activeacute,spanish]{babel}

\begin{document}

¡Hola mundo!

Este es mi primer documento en \LaTeX{}

\end{document}
```

Compilamos el código dando click en la flecha marcada de lado izquierdo de *Compilación rápida* o tambíen podemos compilar ejecutando `Fn + F1`. Así, se obtiene el siguiente **PDF**:

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="../../../../files/Primer_documento.pdf" height="525" width="100%"></iframe>

Este documento **PDF** se generará en la ventana derecha, pero también se guardará en la carpeta donde tengamos el archivo $\LaTeX{}$.