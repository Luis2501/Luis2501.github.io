#!/usr/bin/env python
# coding: utf-8

# <a class="reference internal image-reference" href="index.html"><img alt="Métodos numéricos para físicos" class="align-left" src="portada.png" style="width: 105px;" align="left"/></a>
# 
# <p><em>Este cuaderno contiene un extracto de  las notas de la clase de métodos numéricos impartida por la M.C. María Guadalupe Godina Cubillo a los alumnos de Ingeniería Física en la Facultad de Ciencias Físico Matemáticas de la Universidad Autónoma de Coahuila.</em></p>
# <p><em>Este libro intercativo en línea fue escrito por <a class="reference external" href="https://luis2501.github.io/">Luis Eduardo Sánchez González</a>.  Este material está sujeto a los términos y condiciones de la licencia <a class="reference external" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons CC BY-NC-SA 4.0</a>. Se permite el uso gratuito para cualquier propósito no comercial. El código se publica bajo la <a class="reference external" href="https://opensource.org/licenses/MIT">licencia MIT</a>. </em></p>

# ________________________________________________

# # 2.1 Método de bisección

# Es el método más elemental y antiguo para determinar las raíces de una ecuación. Este método se basa en el **Teorema de Bolzano**. 
#  
# Consideremos una ecuación de tipo $f(x) = 0$, de donde $f(x)$ es una función continua. entonces, puede interpretarse como una condición suficiente para la existencia de soluciones de ese tipo de ecuaciones. Si podemos garantizar la existencia de dos puntos $x_1$ y $x_2$ para los cuales $f(x)$ sea continua en el intervalo $[x_1, x_2]$ y $f(x_1) \cdot f(x_2) < 0$, entonces podemos concluir que existe una solución de la ecuación $f(x) = 0$ en el intervalo anterior. 
# 
# ```{admonition} Nota
# Una manera intuitiva de entender el teorema de Bolzano es observando que si $f(x_1) \cdot f(x_2) < 0$ entonces $f(x_1) < 0$ ó $f(x_2) < 0 $. Esto quiere decir que uno de los puntos se encuentra debajo del eje $x$ y el otro encima de este; además esto implica que la función $f(x)$ necesariamente tiene que pasar por el eje $x$ para llegar de un punto a otro. Por lo tanto, si $f(x)$ es continua entonces debe existir por lo menos un punto que cumpla que $f(x) = 0$.
# ```
# 
# Aunado a eso podemos observar el punto medio de el intervalo $[x_1, x_2]$ llamémosle 
# 
# $$x_m = \frac{x_1 + x_2}{2}$$
# 
# si analizamos este punto tenemos que este punto evaluado en la función puede tomarse como una aproximación a la solución, esto nos lleva a observar dos casos, que $f(x_m) = 0$ ó  que $f(x_m) \neq 0$.
# 
# Cuando $f(x_m) = 0$ entonces el punto medio de este intervalo es una solución exacta para la ecuación $f(x) = 0$ por consiguiente el teorema queda demostrado. En cambio, si $f(x_m) \neq 0$ la solución no se encuentra en el punto medio entonces, aplicando el teorema de
# Bolzano anteriormente visto, tenemos que garantizar la existencia de dos puntos. Ahora nuestros puntos $x_m = x_1$ ó $x_m = x_2$ para los cuales $f(x)$ sea continua en el intervalo $[x_1,x_2]$ y $f(x_1) f(x_2) < 0$, entonces podemos concluir que existe una solución de la ecuación $f(x^{∗}) = 0$.

# ## Ejemplo del método de bisección

# En esta sección se presenta un ejemplo en el cual se requiere encontrar una aproximación a la raíz de un polinomio. La intención del análisis detallado es entender la función que realiza el método. Utilizando el método de bisección. Encontrar una solución aproximada con un error menor que $10^{-5}$ en el intervalo $[1, 2]$ para la función $f(x) = x^3 - 5$.
# Pongamonos en contexto, tenemos un intervalo [a, b] = [1, 2], tomando a = 1 y b = 2 primero que nada para garantizar que existe una raíz, evaluamos los extremos del intervalo en $f(x)$ como se muestra a continuación.

# <div><iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://chart-studio.plotly.com/~luis2501/5.embed" height="525" width="100%"></iframe></div>
# 
