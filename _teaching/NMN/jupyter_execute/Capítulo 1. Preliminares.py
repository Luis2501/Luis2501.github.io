#!/usr/bin/env python
# coding: utf-8

# <a class="reference internal image-reference" href="index.html"><img alt="Métodos numéricos para físicos" class="align-left" src="portada.png" style="width: 105px;" align="left"/></a>
# 
# <p><em>Este cuaderno contiene un extracto de  las notas de la clase de métodos numéricos impartida por la M.C. María Guadalupe Godina Cubillo a los alumnos de Ingeniería Física en la Facultad de Ciencias Físico Matemáticas de la Universidad Autónoma de Coahuila.</em></p>
# <p><em>Este libro intercativo en línea fue escrito por <a class="reference external" href="https://luis2501.github.io/">Luis Eduardo Sánchez González</a>.  Este material está sujeto a los términos y condiciones de la licencia <a class="reference external" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons CC BY-NC-SA 4.0</a>. Se permite el uso gratuito para cualquier propósito no comercial. El código se publica bajo la <a class="reference external" href="https://opensource.org/licenses/MIT">licencia MIT</a>. </em></p>

# ___________________________________

# # Capítulo 1. Preliminares

# Representar el input en la memoria depende de la estructura de la memoria. Por simplicidad y consistencia con el modelo de máquina de acceso aleatoria para computar, la mayoría de las memorias tienen una estructura binaria: muchos contenedores ordenados y distinguidos que pueden pueden tener dos posibles valores.
# 
# >Definimos un bit como un contenedor en una memoria tal que el contenedor solo puede tener dos valores distintos, que denotaremos 0 y 1.
# 
# Ya que la mayoría de operaciones que queremos realizar en una computadora no son sobre objetos binarios, si no sobre objetos más complejos (números enteros, números reales, palabras), debemos codificar esas estructuras en algo binario. A una estructura computacional diseñada para almacenar un dato codificado le llamamos tipo.
