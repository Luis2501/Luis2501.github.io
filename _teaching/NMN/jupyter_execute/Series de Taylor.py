#!/usr/bin/env python
# coding: utf-8

# # Series de Taylor

# Suponga que $ f \in C^{n} \; [a,b] $, que $ f^{(n+1)} $ existe en $ [a, b] $ y $ x_{0}\in [a, b]$. Para cada $ x \in [a, b] $, existe un número $ \varepsilon (x) $ entre $ x_{0}$ y $ x $ tal que 
# 
# $$ f(x) = P_{n} (x) + R_{n} (x) $$
# donde 
# 
# $$ P_{n} (x) = f(x_{0}) + f'(x_{0})(x - x_{0}) + \dfrac{f"(x_{0})(x -x_{0})^{2}}{2!} + \cdots + \dfrac{f^{(n)}(x_{0})(x - x_{0})^{n}}{n!}$$
# 
# $$= \sum_{k=0}^{n} \dfrac{f^{(k)}(x_{0})(x - x_{0})^{k}}{k!}$$
# 
# y 
# 
# $$R_{n} (x) = \dfrac{f^{(n+1)}(\varepsilon (x)) (x - x_{0})^{n+1}}{(n+1)!} $$

# <div><iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~luis2501/3.embed" height="525" width="100%"></iframe></div>

# ## Fórmula de Euler

# Es quizás, la fórmula de Euler, una de las ecuaciones más famosas en las matemáticas, la cual se describe de la siguiente forma
# 
# \begin{equation}
# e^{ix} = \cos(x) + i \sin(x)
# \end{equation}
# 
# donde $i$ es la unidad imaginaria, es decir $i = \sqrt{-1}$. 
# 
# **Demostración:**
# 
# $$\cos(x) = 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + \dfrac{x^{8}}{8!} + ... $$
# $$\sin(x) = x - \dfrac{x^{3}}{3!} + \dfrac{x^{5}}{5!} - \dfrac{x^{7}}{7!} + \dfrac{x^{9}}{9!} + ... $$
# 
# 
# $$e^{x} = 1 + x + \dfrac{x^{2}}{2!} + \dfrac{x^{3}}{3!} + \dfrac{x^{4}}{4!} + \dfrac{x^{5}}{5!} + \dfrac{x^{6}}{6!} + ... $$
# 
# $$e^{ix} = 1 + ix + \dfrac{(ix)^{2}}{2!} + \dfrac{(ix)^{3}}{3!} + \dfrac{(ix)^{4}}{4!} + \dfrac{(ix)^{5}}{5!} + \dfrac{(ix)^{6}}{6!} + ... $$
# 
# $$e^{ix} = 1 + ix - \dfrac{x^{2}}{2!} - \dfrac{ix^{3}}{3!} + \dfrac{x^{4}}{4!} + \dfrac{ix^{5}}{5!} - \dfrac{x^{6}}{6!} + ... $$
# 
# $$e^{ix} = 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + ix - \dfrac{ix^{3}}{3!} + \dfrac{ix^{5}}{5!}  + ... $$
# 
# $$e^{ix} = (1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} + ...) + i(x - \dfrac{x^{3}}{3!} + \dfrac{x^{5}}{5!}  + ... )$$
# 
# Por lo tanto
# 
# $$e^{ix} = \cos(x) + i \sin(x)$$

# ## Movimiento en caida libre

# La caida libre se describe de tal manera que 
# 
# \begin{equation}
# y = y_{0} + v_{0}t - \dfrac{1}{2} g t^{2}
# \end{equation}
# 
# Y si $v = 0$, entonces decimos que 
# 
# \begin{equation}
# y = y_{0} - \dfrac{1}{2}g t^{2}
# \end{equation} 
# 
# \noindent Resulta que cuando dejamos caer un objeto de una cierta altura $y_{0}$, entonces la aceleración a la que estará sujeta el objeto es 
# 
# $$a = \dfrac{d^{2} y}{dt^{2}} = -g$$
# 
# \noindent Sabemos que en $y(0) = y_{0}$ y además $v = y'(0) = 0$. No sabemos la solución a la ecuación diferencial, pero por medio de series de Taylor sabemos que la función solución debe tener este aspecto, en torno a $t = 0$
# 
# $$y = \dfrac{y(0)(t - 0)^{0}}{0!} + \dfrac{y'(0)(t - 0)^{1}}{1!} + \dfrac{y''(0)(t - 0)^{2}}{2!} $$
# $$y = y_{0} + \dfrac{y''(0)(t)^{2}}{2}  $$
# 
# Por lo tanto
# 
# $$y = y_{0} - \dfrac{gt^{2}}{2} =  y_{0} - \dfrac{1}{2}g t^{2} $$

# ## Rotaciones

# $$z = x + iy$$
# $$z_{1} = a + ib$$
# 
# $$z \cdot z_{1} = (x + iy)(a + ib) = (x a - y b) + i(x b + ay)  $$
# 
# $$z' = e^{i \theta} = \cos(\theta) + i \sin(\theta) , \qquad 0 \leq \theta \leq 2 \pi$$
# 
# $$z \cdot z' = z \cdot e^{i \theta} = (x \cos\theta - y \sin \theta) + i(x \sin \theta + y \cos \theta) $$
# 
# Podemo ver al conjunto de los número complejos $\mathbb{C}$ como $\mathbb{R} ^{2}$, es decir que si $z \in \mathbb{C}$
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
# \begin{equation}
#  R = \begin{pmatrix}
#  \cos\theta & - \sin \theta \\
#  \sin \theta &  \cos \theta
# \end{pmatrix}
# \end{equation}
# 
# es la matriz de rotación.
# 
# Definimos
# 
# \begin{equation}
#  A = \begin{pmatrix}
#  0 & -1 \\
#  1 &  0
# \end{pmatrix}
# \end{equation}
# 
# entonces
# 
# \begin{equation}
# R = e^{A \theta} = exp(A \theta)
# \end{equation}
# 
# Demostración:
