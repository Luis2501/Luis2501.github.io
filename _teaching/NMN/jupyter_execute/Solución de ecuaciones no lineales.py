#!/usr/bin/env python
# coding: utf-8

# # Solución de ecuaciones no lineales

# En este capítulo abordaremos uno de los problemas básicos de los métodos numéricos. Si consideramos una función continua $f(x) \in C[a,b]$, el problema de encontrar las raíces de esta función consiste en buscar los valores $x=x_0$ para los cuales se cumple que:
#     
# $$f(x_0) = 0$$
# 
# donde el número $x=x_0$ que hace que se cumpla la condición, se conoce como la raíz de la ecuación $f(x)$ ó cero de la función $f(x)$. El problema de encontrar las raíces de una ecuación es uno de los más importantes problemas computacionales.   
#     
# <br>
# 
# >**Definición:** Un función $f(x)$ es una función lineal si satisface las siguientes propiedades:
# >$$f(x+y)=f(x)+f(y)$$
# >$$f(\alpha x) = \alpha f(x)$$
# >Si esto no se cumple, entonces se dice que la función es no lineal.
# 
# <br>
# Dicho de otra manera, una función lineal es aquella que tiene la forma de un polinomio de primer grado, es decir las incógnitas no estan elevadas a potencias ni multiplicadas entre sí. Por ejemplo, las funciones
# 
# $$ 3x+3y=4, \qquad \qquad 3x -5y+7z=9$$
# 
# \noindent son funciones lineales. En cambio, las funciones
# 
# $$x^2+x = 2, \qquad \qquad x+sin^2 x + e^x =0$$
# 
# no son funciones lineales. 
# 
# <br>
# 
# Debemos notar que la solución de la ecuación $f(x) = 0$ puede ser muy difícil dependiendo de la naturaleza de $f(x)$. Por ejemplo, si $f(x)$ es un polinomio de grado mayor o igual que 4, o bien no es polinómica, no hay ninguna fórmula conocida de solución. Por ejemplo, el caso de un polinomio de grado 2, sabemos que la solución está dado por
#     
# $$x=\frac{-b \pm \sqrt{b^2-4ac}}{2a}$$
# 
# Así, salvo pocas excepciones, no es posible encontrar expresiones analíticas para hallar las raíces. Ante esto, surge la  necesidad de usar métodos numéricos. 
# 
# ```{admonition} Nota
# En Python es muy sencillo definir función de la forma $f(x)$, para esto podemos utilizar la función *lambda*. Por ejemplo, para expresar $f(x) = x^2 + x +5 $, debemos escribir, 
# 
# `f = lambda x: x*x + x + 5`
#     
# Este código puede reproducirlo para cualquier función $f(x)$. 
# ```
# 
# 
# 
