#!/usr/bin/env python
# coding: utf-8

# <a class="reference internal image-reference" href="index.html"><img alt="Métodos numéricos para físicos" class="align-left" src="portada.png" style="width: 105px;" align="left"/></a>
# 
# <p><em>Este cuaderno contiene un extracto de  las notas de la clase de métodos numéricos impartida por la M.C. María Guadalupe Godina Cubillo a los alumnos de Ingeniería Física en la Facultad de Ciencias Físico Matemáticas de la Universidad Autónoma de Coahuila.</em></p>
# <p><em>Este libro intercativo en línea fue escrito por <a class="reference external" href="https://luis2501.github.io/">Luis Eduardo Sánchez González</a>.  Este material está sujeto a los términos y condiciones de la licencia <a class="reference external" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons CC BY-NC-SA 4.0</a>. Se permite el uso gratuito para cualquier propósito no comercial. El código se publica bajo la <a class="reference external" href="https://opensource.org/licenses/MIT">licencia MIT</a>. </em></p>
# 

# ______________________________

# # 1.2 Series de Taylor

# Supongamos tener una función arbitraría $f(x)$ e intentaremos hacer es aproximar a la función $f$ con un polinomio, al cual le agregaremos más sumandos.
# 
# ```{margin} Función $f(x)$ arbitraria
# <img src="Taylor.png">
# Para aproximar $f(x)$ supondremos que existe $f(0)$ y además $f^{n}(0)$
# ```
# 
# Para esto supongamos que $f(0)$ existe, como se muestra en la figura anterior, además que la función es derivable n veces, y que $f^{(n)} (0)$ también existe, es decir que existen los siguientes números
# 
# $$f(0), f'(0), f''(0), f'''(0), ... $$
# 
# Aqui surge una pregunta, ¿Cómo podemos aproximar esto con polinomios que van aumentando en longitud?
# 
# Empezemos con un polinomio constante, es decir un polinomio de grado 0, es sencillo, 
# 
# $$P(0) = f(0) \qquad \Rightarrow \qquad P(x) = f(0) $$
# 
# Este polinomio $P$ solo coincide en un punto con la función $f$, por lo que no es muy buena aproximación. Si además también queremos que
# 
# $$P'(0) = f'(0)$$
# 
# Entonces el polinomio lo podemos escribir como
# 
# $$P(x) = f(0) + f'(0) x$$
# 
# Sin perder la primera restricción esto se puede hacer, ya que si tomamos
# 
# $$P(0) = f(0)$$
# 
# y
# 
# $$P'(0) = f'(0)$$
# 
# podemos observar que se cumplen las condiciones. Ya tenemos una mejor aproximación, dado que el polinomio $P$ coincide en dos puntos, pero sigue sin ser una excelente aproximación.
# 
# Ahora, propondremos que el polinomio sea
# 
# $$P(x) = f(0) + f'(0) x + \frac{1}{2} f''(0) x^2$$
# 
# No es muy difícil observar que 
# 
# $$P(0) = f(0), \qquad P'(0) = f'(0), \qquad P''(0) = f''(0)$$
# 
# Más puntos coinciden, esto implica que cada vez el polinomio se parece más a $f(x)$. También debemos notar que existe un patrón al ir agregando ciertos términos, así, podemos aproximar a $f(x)$ a un polinomio de grado $n$ tal que
# 
# $$P(x) = f(0) + f'(0) x + \frac{1}{2} f''(0) x^2 + \frac{1}{3!} f'''(0) x^3 + ... + \frac{1}{n!} f^{(n)} (0) x^n$$
# 
# Con este polinomio 

# También una función $f(x)$ puede escribirse como un polinomio de Taylor, es decir como una serie que se trunca, así
# 
# $$ f(x) = P_{n} (x) + R_{n} (x) $$
# 
# donde 
# 
# $$ P_{n} (x) = f(x_{0}) + f'(x_{0})(x - x_{0}) + \dfrac{f"(x_{0})(x -x_{0})^{2}}{2!} + \cdots + \dfrac{f^{(n)}(x_{0})(x - x_{0})^{n}}{n!}$$
# 
# $$= \sum_{k=0}^{n} \dfrac{f^{(k)}(x_{0})(x - x_{0})^{k}}{k!}$$
# 
# y 
# 
# $$R_{n} (x) = \dfrac{f^{(n+1)}(\varepsilon (x)) (x - x_{0})^{n+1}}{(n+1)!} $$
# 
# se le conoce como el **residuo** del polinomio.

# ## Serie de Maclaurin de $e^{x}$
# 
# Para obtener la serie de Maclaurin de $f(x) = e^{x}$, debemos considerar la derivada $n$-esima de $f$, pero sabemos que la derivada de la exponencial siempre es la misma exponencial, entonces
# 
# $$f^{n} (x) = e^{x}$$
# 
# y evaluando en cero se tiene
# 
# $$f^{n} (0) = e^{0} = 1$$
# 
# Esto implica que la serie de Taylor de $e^{x}$ se escribe como
# 
# $$e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!}$$
# 
# es decir que
# 
# $$e^{x} = \sum_{k = 0} ^{\infty} \frac{x^{k}}{k!}$$
# 
# podriamos decir que es la serie más sencilla de obtener debido a esa característica en su derivada.

# ## Serie de Maclaurin de $\cos(x)$
# 
# Considerando la función $f(x) = \cos(x)$

# ## Serie de Maclaurin de $\sin(x)$
# 
# Dada la función $f(x) = \sin(x)$

# Estos resultados podemos observarlos en la siguiente gráfica. La cual muestra los primeros 10 polinomios de Taylor de las funciones antes mencionadas. 

# <iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="Taylor.html" height="525" width="100%"></iframe>

# ## Aplicaciones de las series de Taylor

# Las series de Taylor y en particular las series de Maclaurin pueden tener múltiples aplicaciones tanto en matemáticas como en física. Para ilustrar esto se seleccionaron algunos ejemplos de aplicación que pueden ser útiles.

# ### Fórmula de Euler 

# La fórmula de Euler, es quizás una de las ecuaciones más famosas en las matemáticas, la cual se escribe de la siguiente forma:
# 
# $$e^{ix} = \cos(x) + i \sin(x)$$
# 
# donde $i$ es la unidad imaginaria, es decir $i = \sqrt{-1}$. Esta fórmula puede demostrarse mediante series de Taylor, en particular series de Maclaurin de ciertas funciones conocidas.
# 
# Para demostrar la fórmula de Euler, debemos considerar la serie de Maclaurin de $e^x$, 
# 
# $$e^{x} = 1 + x + \dfrac{x^{2}}{2!} + \dfrac{x^{3}}{3!} + \dfrac{x^{4}}{4!} + \dfrac{x^{5}}{5!} + \dfrac{x^{6}}{6!} + ... $$
# 
# Así, si en lugar de $e^x$ tomamos $e^{ix}$ tendremos que
# 
# $$e^{ix} = 1 + ix + \dfrac{(ix)^{2}}{2!} + \dfrac{(ix)^{3}}{3!} + \dfrac{(ix)^{4}}{4!} + \dfrac{(ix)^{5}}{5!} + \dfrac{(ix)^{6}}{6!} + ... $$
# 
# Por lo que, elevando la $i$ en cada uno de los términos, se tendra lo siguiente,
# 
# $$e^{ix} = 1 + ix - \dfrac{x^{2}}{2!} - \dfrac{ix^{3}}{3!} + \dfrac{x^{4}}{4!} + \dfrac{ix^{5}}{5!} - \dfrac{x^{6}}{6!} + ... $$
# 
# Ahora, si separamos la parte real y la parte imaginaria,
# 
# $$e^{ix} = 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + ix - \dfrac{ix^{3}}{3!} + \dfrac{ix^{5}}{5!}  + ... $$
# 
# y para visualizar mejor reescribimos de la siguiente manera
# 
# $$e^{ix} = \left( 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + ... \right) + i \left( x - \dfrac{x^{3}}{3!} + \dfrac{x^{5}}{5!}  + ... \right)$$
# 
# Por último, debemos observar que la parte real es la serie de Maclaurin de $\cos(x)$,
# 
# $$\cos(x) = 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + \dfrac{x^{8}}{8!} + ... $$
# 
# Y que la parte imaginaria es la serie de Maclaurin de $\sin(x)$,
# 
# $$\sin(x) = x - \dfrac{x^{3}}{3!} + \dfrac{x^{5}}{5!} - \dfrac{x^{7}}{7!} + \dfrac{x^{9}}{9!} + ... $$
# 
# Por lo tanto, obtenemos que
# 
# $$e^{ix} = \cos(x) + i \sin(x)$$
# 
# Que es lo que queriamos demostrar. Apartir de esta fómula podemos llegar a lo que se conoce como la **identidad de Euler**, por algunos considera una belleza de las matemáticas. Si en la fórmula de Euler tomamos $x= \pi$, se tiene
# 
# $$e^{i \pi} = -1$$
# 
# Por lo tanto,
# 
# $$e^{i\pi} + 1 = 0$$
# 
# Como hemos dicho, esta identidad es considerada una belleza matemática, y esto se debe a que esta identidad vincula números de distintas áreas de las matemáticas que parecen distintas y sin relación alguna a simple vista.

# ### Movimiento en caida libre

# Cuando dejamos caer un objeto desde cierta altura $y_0$, el movimiento puede ser descrito mediante una de las ecuaciones más conocidas en física básica,
# 
# $$y(t) = y_{0} + v_{0}t - \dfrac{1}{2} g t^{2}$$
# 
# Y dado que dejamos caer el objeto, la velocidad $v_{0} = 0$, entonces decimos que 
# 
# $$y(t) = y_{0} - \dfrac{1}{2}g t^{2}$$
# 
# Esta fórmula puede demostrarse mediante series de Taylor. Resulta que cuando dejamos caer un objeto de una cierta altura $y_{0}$, entonces la aceleración a la que estará sujeta el objeto es 
# 
# $$a = y''(t) = -g$$
# 
# tenemos una ecuación diferencial. Si ya sabes cómo resolver ecuaciones diferenciales, seguramente esta ecuación te parecera trivial. Sin embargo en esta ocasión intentaremos darle un enfoque distinto. 
# 
# Sabemos que $y(0) = y_{0}$ es la altura a la que se deja caer el objeto y además $v = y'(0) = 0$. Por medio de series de Taylor sabemos que podemos expresar la función $y$ de la siguiente manera
# 
# $$y(t) = \dfrac{y(0)(t - 0)^{0}}{0!} + \dfrac{y'(0)(t - 0)^{1}}{1!} + \dfrac{y''(0)(t - 0)^{2}}{2!} + ... $$
# 
# truncando la serie para tres términos y tomando en cuenta las condiciones que se presentaron, la expresión se puede reducir a
# 
# $$y(t) = y_{0} + \dfrac{y''(0)t^{2}}{2}  $$
# 
# Y como sabemos cual es el valor de $y''(0)$, entonces
# 
# $$y(t) =  y_{0} - \dfrac{1}{2}g t^{2}$$
# 
# que es la expresión a la que sabiamos teniamos que llegar.

# ### Rotaciones

# Las series de Taylor también son capaces de explicar las rotaciones, esas trasnformaciones que muy seguramente viste en álgebra lineal. Para comenzar supongamos tener dos números complejos,
# 
# $$z = x + iy \qquad \wedge \qquad w = a + ib$$
# 
# recordemos que la multiplicación de dos números es de la siguiente manera
# 
# $$z \cdot w = (x + iy)(a + ib) = (x a - y b) + i(x b + ay)  $$
# 
# Entonces, sabemos que un número complejo podemos expresarlo en términos de la fórmula de Euler,por lo que, si consideramos un número complejo de módulo unitario se puede escribir como
# 
# $$z' = e^{i \theta} = \cos(\theta) + i \sin(\theta) , \qquad 0 \leq \theta \leq 2 \pi$$
# 
# y si multiplicamos este número por $z$, 
# 
# $$z \cdot z' = z \cdot e^{i \theta} = (x \cos\theta - y \sin \theta) + i(x \sin \theta + y \cos \theta) $$
# 
# Para observar de diferente manera esta multiplicación, recordemos que podemos ver al conjunto de los número complejos $\mathbb{C}$ como $\mathbb{R} ^{2}$, es decir que si $z \in \mathbb{C}$
# 
# $$z = \begin{pmatrix}
# \; x \; \\ 
# \; y \;
# \end{pmatrix} $$
# 
# Rescribiendo de esta manera $z \cdot z'$, tenemos
# 
# $$z \cdot z' = \begin{pmatrix}
# x \cos\theta - y \sin \theta \\
# x \sin \theta + y \cos \theta
# \end{pmatrix} = \begin{pmatrix}
#  \cos\theta & - \sin \theta \\
#  \sin \theta &  \cos \theta
# \end{pmatrix} \cdot \begin{pmatrix}
# \; x \; \\ 
# \; y \;
# \end{pmatrix} $$
# 
# Donde diremos que 
# 
# $$ R = \begin{pmatrix}
#  \cos\theta & - \sin \theta \\
#  \sin \theta &  \cos \theta
# \end{pmatrix}$$
# 
# es lo que se conoce como **matriz de rotación**. Si no recuerdas como ocurren las rotaciones te dejo una animación del canal [3Blue1BrowmClips](https://www.youtube.com/channel/UCm_vjtdNgTHzFzkRfItPR-w)

# <br>
# 
# <iframe width="100%" height="400" src="https://www.youtube.com/embed/Z7JyPYgsefc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# <br>

# Más aún importante, debemos observar que $e^{i \theta}$ nos está describiendo una rotación. Es algo impresionante, ya que si recuerdas tus clases de álgebra lineal, las rotaciones solo ocurrian con matrices y vectores. Para poder entender porque esta expresión es una rotación consideremos tener la siguiente matriz
# 
# $$ A = \begin{pmatrix}
#  0 & -1 \\
#  1 &  0
# \end{pmatrix}$$
# 
# esta matriz tiene algo muy interesante, ya que 
# 
# $$ A^2 = \begin{pmatrix}
#  -1 & 0 \\
#  0 &  -1
# \end{pmatrix} = - \begin{pmatrix}
#  1 & 0 \\
#  0 & 1
# \end{pmatrix} = - I$$
# 
# lo cual es impresionate, debido que $i^2 = -1$. Esto nos conduce a preguntarnos, ¿Existira una fórmula de Euler que en lugar de $i$ tenga $A$?, es decir que se cumpla que
# 
# $$e^{A \theta} = cos(\theta) + A \sin(\theta)$$
# 
# Y esto resulta que si es posible. Para demostrarlo, tomemos la serie de Taylor de $e^{A \theta}$, 
# 
# $$e^{Ax} = 1 + Ax + \dfrac{(Ax)^{2}}{2!} + \dfrac{(Ax)^{3}}{3!} + \dfrac{(Ax)^{4}}{4!} + \dfrac{(Ax)^{5}}{5!} + \dfrac{(Ax)^{6}}{6!} + ... $$
# 
# Como $A^{2} = -1$ entonces $A^{3} = A^{2} A= -A$ y $A^{4} = A^{2} A^{2} = 1$, es decir que $A$ tiene el mismo comportamiento que $i$, así
# 
# $$e^{Ax} = 1 + Ax - \dfrac{x^{2}}{2!} - \dfrac{Ax^{3}}{3!} + \dfrac{x^{4}}{4!} + \dfrac{Ax^{5}}{5!} - \dfrac{x^{6}}{6!} + ... $$
# 
# Ahora, si separamos la parte real y la parte imaginaria,
# 
# $$e^{Ax} = 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + Ax - \dfrac{Ax^{3}}{3!} + \dfrac{Ax^{5}}{5!}  + ... $$
# 
# y nuevamente para visualizar mejor reescribimos de la siguiente manera
# 
# $$e^{Ax} = \left( 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + ... \right) + A \left( x - \dfrac{x^{3}}{3!} + \dfrac{x^{5}}{5!}  + ... \right)$$
# 
# Por lo tanto se tiene que
# 
# $$e^{A \theta} = cos(\theta) + A \sin(\theta)$$
# 
# que de forma matricial tendremos
# 
# $$e^{A \theta} = \begin{pmatrix}
#  \cos \theta & 0 \\
#  0 &  \cos \theta
# \end{pmatrix} + \begin{pmatrix}
#  0 & - \sin \theta \\
#  \sin \theta &  0
# \end{pmatrix} = \begin{pmatrix}
#  \cos \theta & - \sin \theta \\
#  \sin \theta &  \cos \theta
# \end{pmatrix}$$
# 
# Por lo tanto, podemos observar que
# 
# $$R = e^{A \theta}$$
# 
# Este resultado es algo muy interesante e impresionante, tenemos dos manera de expresar una rotación, y una de ellas es elevando un número ($e$) a una matriz, algo que quizás no habrias pensado hasta ahora.
