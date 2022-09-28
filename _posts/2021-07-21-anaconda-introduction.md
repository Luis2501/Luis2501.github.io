---
layout: post
title: "Anaconda: Una suite para científicos (SPA)"
date: 2021-07-21 15:02:15
description: Introducción e instalación de Anaconda
tags:
  - anaconda
  - python
  - code
categories: tutorial
---

<p style="text-align: justify">
Python es un lenguaje de programación de alto nivel, interpretado y multiparadigma. Cuenta con una gramática simple y sencilla, lo cual hace que Python sea facil de aprender y de usar. Además, Python es un lenguaje muy popular y usado por organizaciones como Google, NASA, la CIA y Disney. También aplicaciones como Netflix, Instagram y Spotify utilizan Python. 
</p>

<p style="text-align: justify">
Una de las características que hace especial a Python es debido a que es multiproposito, esto quiere decir que es usado para muchos fines. Entre ellos son aplicaciones web, ciencia de datos, juegos, modelos de machine learning, computación científica, entre otras cosas.
</p>

<p style="text-align: justify">
Para trabajar con Python y poder aprovechar al máximo lo que ofrece este lenguaje y sus herramientas en cuestión de ciencia de datos, computación científica, etc, debemos usar una de sus distribuciones: <b><a href="https://www.anaconda.com/" target="_blank">Anaconda</a></b> 
</p>

<p style="text-align: justify">
<b>Anaconda</b> es una suite de código abierto que abarca una serie de aplicaciones, librerías y conceptos diseñados para el desarrollo de la ciencia de datos con Python. Esta suite de herramientas está diseñada para la ciencia de datos con Python pero es útil para la mayoría de los desarrolladores con Python, ya que cuenta con una gran cantidad de aplicaciones y paquetes que nos permitirán ser más eficientes.
</p>

<p style="text-align: justify">
De manera general Anaconda es una distribucción de Python que funciona como un gestor de entorno, un gestor de paquetes y que posee una colección de más de 720 paquetes de código abierto.
</p>

<p style="text-align: justify">
Anaconda se agrupa en 4 sectores o soluciones tecnológicas, <b>Anaconda Navigator</b>, <b>Anaconda Project</b>, <b>librerías científicas</b> y <b>conda</b>. Todas estás se instalan de manera automática y en un procedimiento muy sencillo.
</p>

<p style="text-align: justify">
En este posts no solamente quiero hablar de Anaconda, sus ventajas y demás. Principalmente la intención de esta publicación es para llevar acabo la instalación de Anaconda y de manera paralela lo puedas hacer.
</p>

# Instalación de Anaconda

Como primer paso para instalar Anaconda, deberas descargar el instalador en el siguiente enlace: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

<a href="https://www.anaconda.com/products/individual" target="_blank"><img src="../../../../images/Instalador.png" alt="Imagen"></a>

Al final de la página encontraras los enlaces para descargar el instalador, dependiendo el sistema operativo y arquitectura de tu computadora.

_______________________

## Windows

Al momento de que se haya descargado el archivo (.exe), deberas ejecutarlo haciendo click. Te aparecera una venta como la siguiente

<img src="../../../../images/Windows_1.png" alt="Imagen 1" align="center">

Haces click en *Next* y luego haces click en *I Agree*

<img src="../../../../images/Windows_2.png" alt="Imagen 2" align="center">

Seleccionas *All Users* y haces click en *Next*

<img src="../../../../images/Windows_3.png" alt="Imagen 3" align="center">

Deberas aceptar los permisos de administrador. Después haces click en *Next*

<img src="../../../../images/Windows_4.png" alt="Imagen 4" align="center">

Seleccionas *Add Anaconda3 to the system PATH enviroment variable* y haga click en *Install*

<img src="../../../../images/Windows_5.png" alt="Imagen 5" align="center">

Esperas a que finalice la instalación y haces click en *Next*

<img src="../../../../images/Windows_6.png" alt="Imagen 6" align="center">

Luego casi por terminar, nuevamente haces click en *Next*

<img src="../../../../images/Windows_7.png" alt="Imagen 7" align="center">

Por último click en *Finish*

<img src="../../../../images/Windows_8.png" alt="Imagen 8" align="center">

Y habras acabado. Tienes instalado Anaconda en tu dispostivo.

___________________________

## Linux

<p style="text-align: justify">
Debo aclarar que la siguiente instalación es mediante Debian/Ubuntu. Antes de comenzar a instalar, debe abrir una terminal y ejecutar los siguiente comandos
</p>

``` console
sudo apt-get update
```

y 

``` console
sudo apt upgrade
```

Ahora, terminada la descarga del archivo de instalación (.sh), debera abrir una terminal en donde se encuentre el archivo, ya sea mediante `cd Descargas` o `cd Downloads`. Después ejecute 


``` console
bash ~nombre_archivo.sh
```

Generalmente el archivo es nombrado como `Anaconda3-2021.05-Linux-x86_64.sh`. Al ejecutar el comando apareceran una serie de instrucciones que debe seguir. 

Al terminar la instalación reinicie su computadora. Y ya reiniciada ejecute `Ctrl + Alt + T` para abrir una terminal y debera aparecer algo como lo siguiente

<img src="../../../../images/Linux_1.png" alt="Imagen 9" align="center">

Esto nos indica que Anaconda sea ha instaldo. La palabra `(base)` antes del prompt indica que nos encontramos en el entorno base de Anaconda. Quizás después hable un poco acerca de los entornos virtuales de Anaconda.

________________________

Anaconda promete ser una suite muy útil no solamente para científicos de datos, si no también para científicos en general (matemáticos, físico, químicos, biólogos, ingenieros, etc). En publicaciones posteriores hablare más acerca de Anaconda. 
