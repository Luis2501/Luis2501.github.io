#!/usr/bin/env python
# coding: utf-8

# # Método de bisección

# Es el método más elemental y antiguo para determinar las raíces de una ecuación. Este método se basa en el **Teorema de Bolzano**. 
#  
# Consideremos una ecuación de tipo $f(x) = 0$, de donde $f(x)$ es una función continua. entonces, puede interpretarse como una condición suficiente para la existencia de soluciones de ese tipo de ecuaciones. Si podemos garantizar la existencia de dos puntos $x_1$ y $x_2$ para los cuales $f(x)$ sea continua en el intervalo $[x_1, x_2]$ y $f(x_1) \cdot f(x_2) < 0$, entonces podemos concluir que existe una solución de la ecuación $f(x) = 0$ en el intervalo anterior. 
# ```{admonition} Nota
# Una manera intuitiva de entender el teorema de Bolzano es observando que si $f(x_1) \cdot f(x_2) < 0$ entonces $f(x_1) < 0$ ó $f(x_2) < 0 $. Esto quiere decir que uno de los puntos se encuentra debajo del eje $x$ y el otro encima de este; además esto implica que la función $f(x)$ necesariamente tiene que pasar por el eje $x$ para llegar de un punto a otro. Por lo tanto, si $f(x)$ es continua entonces debe existir por lo menos un punto que cumpla que $f(x) = 0$.
# ```
# 
# Aunado a eso podemos observar el punto medio de el intervalo $[x_1, x_2]$ llamémosle 
# 
# $$x_m = \frac{x_1 + x_2}{2}$$
# 
# si analizamos este punto tenemos que este punto evaluado en la función puede tomarse como una aproximación a la solución, esto nos lleva a observar dos casos, que $f(x_m) = 0$ o  que $f(x_m) \neq 0$.
# 
# Cuando $f(x_m) = 0$ entonces el punto medio de este intervalo es una solución exacta para la ecuación $f(x) = 0$ por consiguiente el teorema queda demostrado.

# <div><iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://chart-studio.plotly.com/~luis2501/5.embed" height="525" width="100%"></iframe></div>
# 
