---
layout: page
title: Python Avanzado Plotly
description: FCFM, UAdeC
img: assets/img/2.jpg
importance: 2
category: Courses
---

<button name="Curso" class="btn"><img align = "left" alt = "Python" width = "15px" src = "https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/jupyter.svg"/> &nbsp; <a style="text-decoration:none; color: inherit" href="https://colab.research.google.com/drive/1_jVjekK2jIcs0TWyiNhU8bjaYyGe-vWS?usp=sharing">Notebook de trabajo</a> </button> 

Taller presentado en la Feria de Ciencia y Tecnología 2022 por parte de la Facultad de Ciencias Físico Matemáticas, UAdeC.

<p style="text-align: justify">
<b>Objetivo:</b> Este taller tiene como objetivo mostrar un poco acerca de la librería Plotly, que consiste en la creación de gráficos científicos interactivos. El taller se llevará a cabo de tal manera que se muestran algunos aspectos avanzados de Python, como los son los distintos paradigmas con los que cuenta Python y también de funciones muy utilizadas de librerías como Numpy y Pandas.
</p>

De preferencia para el taller se debe tener instalado Python con Anaconda, en caso contrario puede consultar el siguiente tutorial para instalar: [Anaconda: Una suite para científicos](https://luis2501.github.io/). 

También se requiere manejar un poco Jupyter Notebook o Google Colab, el siguiente video muestra un pequeño tutorial acerca de herramientas para programar en Python: [Herramientas para programar en Python](https://www.youtube.com/watch?v=rePT-jSmer4). 

<!--## Instalación de Plotly 

Como primer paso para instalar Plotly, debemos ubicar donde podemos encontrar cualquier paquete de Python, que es en el siguiente enlace: [https://anaconda.org/](https://anaconda.org/).

<a href="https://anaconda.org/" target="_blank"><img src="https://luis2501.github.io/files/Taller_Python_Avanzado/Instalacion_1.png" alt="Imagen 1"></a>

Esta página nos muestra un navegador y un formulario para poder registrarnos. Registrarse **NO** es necesario, solamente es necesario usar el navegador para buscar el paquete que buscamos. Por ejemplo en el caso de querer instalar Plotly solo debemos escribir *Plotly* en el navegador y pulsar `Enter`:

<a href="https://anaconda.org/" target="_blank"><img src="https://luis2501.github.io/files/Taller_Python_Avanzado/Instalacion_2.png" alt="Imagen 1"></a>

Después nos aparecerá una lista con todos los posibles paquetes con ese nombre, debemos buscar el que queremos, en este caso es el que tiene mayor número de descargas, el primero en la lista que aparece como *conda-forge/plotly*.

<a href="https://anaconda.org/search?q=plotly" target="_blank"><img src="https://luis2501.github.io/files/Taller_Python_Avanzado/Instalacion_3.png" alt="Imagen 1"></a>

Damos click en esa opción y nos aparecerá algo como lo siguiente:

<a href="https://anaconda.org/conda-forge/plotly" target="_blank"><img src="https://luis2501.github.io/files/Taller_Python_Avanzado/Instalacion_4.png" alt="Imagen 1"></a>

En este apartado nos aparece la información del paquete, como su documentación, donde se encuentra alojado, su sitio web y una pequeña descripción. Más abajo nos aparecen los instaladores, los que se encuentran como `conda install -c conda-forge plotly` son los que nos interesan. 

A continuación se mostrará como instalar el paquete en los distintos sistemas operativos. Este proceso aplica para cualquier paquete que deseé instalar.

Para el taller también requeriremos instalar *Plotly Express* que se encuentra en la lista antes mencionado más abajo.

<a href="https://anaconda.org/search?q=plotly" target="_blank"><img src="https://luis2501.github.io/files/Taller_Python_Avanzado/Instalacion_5.png" alt="Imagen 1"></a> -->

____________

### Windows

Para instalar cualquier paquete de Python con Anaconda debes abrir el prompt de Anaconda. Abre el buscador de windows (o pulsa la tecla windows) y escribe *Anaconda prompt*. La aplicación que te aparezca deberás dar click derecho y luego pulsar *Ejecutar como administrador*. 

Después de eso se abrirá una terminal y debes ejecutar el comando de instalación que antes nos apareció, es decir

``` console
conda install -c conda-forge plotly
```

Deberas esperar a que en algún momento nos pida escribir `y` para aceptar y después solamente falta esperar a que se instale. Esto también debes hacer para instalar Plotly Express. 

______________________________________

### Linux

<p style="text-align: justify">
Debo aclarar que la siguiente instalación es mediante Debian/Ubuntu. Antes de comenzar a instalar, debe abrir una terminal con `Ctrl + T` y ejecutar los siguiente comandos
</p>

``` console
sudo apt-get update
```

y 

``` console
sudo apt upgrade
```

Después debes ejecutar el comando de instalación que se mostraba en la página, el caso de Plotly es 

``` console
conda install -c conda-forge plotly
```

Deberas esperar a que en algún momento nos pida escribir `y` para aceptar y después solamente falta esperar a que se instale. Esto también debes hacer para instalar Plotly Express. 




