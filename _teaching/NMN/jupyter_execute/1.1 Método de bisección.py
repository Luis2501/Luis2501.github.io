#!/usr/bin/env python
# coding: utf-8

# # 1.1 Método de bisección

# Es el método más elemental y antiguo para determinar las raíces de una ecuación. Este método se basa en el **Teorema de Bolzano**. 
#  
# Consideremos una ecuación de tipo $f(x) = 0$, de donde $f(x)$ es una función continua. entonces, puede interpretarse como una condición suficiente para la existencia de soluciones de ese tipo de ecuaciones. Si podemos garantizar la existencia de dos puntos $x_1$ y $x_2$ para los cuales $f(x)$ sea continua en el intervalo $[x_1, x_2]$ y $f(x_1) \cdot f(x_2) < 0$, entonces podemos concluir que existe una solución de la ecuación $f(x) = 0$ en el intervalo anterior. 
