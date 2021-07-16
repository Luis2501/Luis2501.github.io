#!/usr/bin/env python
# coding: utf-8

# <a class="reference internal image-reference" href="index.html"><img alt="Métodos numéricos para físicos" class="align-left" src="portada.png" style="width: 105px;" align="left"/></a>
# 
# <p><em>Este cuaderno contiene un extracto de  las notas de la clase de métodos numéricos impartida por la M.C. María Guadalupe Godina Cubillo a los alumnos de Ingeniería Física en la Facultad de Ciencias Físico Matemáticas de la Universidad Autónoma de Coahuila.</em></p>
# <p><em>Este libro intercativo en línea fue escrito por <a class="reference external" href="https://luis2501.github.io/">Luis Eduardo Sánchez González</a>.  Este material está sujeto a los términos y condiciones de la licencia <a class="reference external" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons CC BY-NC-SA 4.0</a>. Se permite el uso gratuito para cualquier propósito no comercial. El código se publica bajo la <a class="reference external" href="https://opensource.org/licenses/MIT">licencia MIT</a>. </em></p>

# ___________________________________

# # Capítulo 2. Solución de ecuaciones no lineales

# En este capítulo abordaremos uno de los problemas básicos de los métodos numéricos. Si consideramos una función continua $f(x) \in C[a,b]$, el problema de encontrar las raíces de esta función consiste en buscar los valores $x=x_0$ para los cuales se cumple que:
#     
# $$f(x_0) = 0$$
# 
# donde el número $x=x_0$ que hace que se cumpla la condición, se conoce como la raíz de la ecuación $f(x)$ ó cero de la función $f(x)$. El problema de encontrar las raíces de una ecuación es uno de los más importantes problemas computacionales.   
# 
# ```{admonition} Definición
# Un función $f(x)$ es una función lineal si satisface las siguientes propiedades:
# 
# $f(x+y)=f(x)+f(y)$
# 
# $f(\alpha x) = \alpha f(x)$
# 
# Si esto no se cumple, entonces se dice que la función es no lineal.
# ```
# 
# Dicho de otra manera, una función lineal es aquella que tiene la forma de un polinomio de primer grado, es decir las incógnitas no estan elevadas a potencias ni multiplicadas entre sí. Por ejemplo, las funciones
# 
# $$ 3x+3y=4, \qquad \qquad 3x -5y+7z=9$$
# 
# son funciones lineales. En cambio, las funciones
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

# ## Funciones matemáticas en Python

# En Python es muy sencillo definir una función matemática $f(x)$, para esto podemos utilizar la función `lambda`. Por ejemplo, para expresar una función arbitraria $f(x)$, la función `lambda` sigue la siguiente sintaxis
# 
# ``` python
# f = lambda x: f(x)
# ```
# 
# Así, por ejemplo, si tenemos $f(x) = x^3 - 2x^2 + 4$, en Python se traduce en

# In[1]:


f = lambda x: x**3 -2*(x**2) + 4


# Y para evaluar en alguna $x$, por ejemplo $x=5$

# In[2]:


f(5) 


# Esto se puede reproducir para cualquier función $f(x)$, sin embargo, si queremos funciones trascendentes (trigonométricas, logartimos, exponenciales) debemos utilizar el módulo `math`. Para esto importamos el módulo de la siguiente manera

# In[3]:


import math


# De esta manera, si queremos por ejemplo las funciones $f(x) = e^{x}$ y $g(x) = \sin x$, debemos escribir

# In[4]:


f = lambda x: math.exp(x)

g = lambda x: math.sin(x)


# Por último, debemos resaltar, que lo anterior también puede ser aplicado a funciones de varias variables. Si tenemos 
# 
# $$f(x,y) = x^2 + y^2$$
# 
# entonces podemos escribirlo en Python como

# In[5]:


f = lambda x,y: x**2 + y**2


# Evaluando en (1,1), se tiene

# In[6]:


f(1,1)

