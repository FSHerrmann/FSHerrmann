# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:27:06 2021

@author: feeli
Essa parte do programa servida para criar a funções de linearização, sua
aplicação e a crianção do gráfico final se dará em outro programa.
"""
# Boa parte achei neste link:

import importlib
import sympy
import math
import sympy
import numpy as np
import matplotlib.pyplot as plt

f = open("Reduzido.txt", "r")
valores = [[float(entry) for entry in line.split()] for line in f.readlines()]
f.close()
valores[0][0] = float(1)
valores[1][0] = float(2)
valores[2][0] = float(3)
valores[3][0] = float(3.5)
valores[4][0] = float(4)

print("Os valores reduzidos são: ", valores)

# Vou adicionar os pontos, como em 2, sem linearizar e plotar ainda
for x in range(0, 5):
    plt.plot(valores[x][0], valores[x][1], "ro")

x = sympy.Symbol('x')
sympy.init_printing()
p = 0


# Vou fazer a liearização dos pontos, usei como referência a página:
# https://sites.google.com/site/cnumer3q16/atividade4?tmpl=%2Fsystem%2Fapp%2Ftemplates%2Fprint%2F&showPrintDialog=1
def Lagrange(z, xn):
    altura = [1, 2, 3, 3.5, 4]
    y = [0.426, 0.714, 0.782, 0.8168, 0.874]
    xf = xn+z
    xu = xn
    p = 0
    for j in range(xu, xf):
        resultado = 1
        for i in range(0, z):
            if (xn != i):
                resultado = resultado*((x-altura[i])/(altura[xn]-altura[i]))
        print(resultado)
        p = p+(resultado*(y[j]))
        xn = xn + 1
    print(p)




# Imprimir os 5
for x in range (0, 5):
    print(Lagrange(5, 0))

# Expandir a equação:
p = 0.426*(3/2 - x/2)*(2 - x) + 0.714*(3 - x)*(x - 1) + 0.782*(x/2 - 1/2)*(x - 2)
sympy.expand(p)


# Cálculo das raízes:
def Delta():
    lista = [0.961, -3.666, 3.522]
    d = ((lista[1])**(2))-(4*(lista[0])*(lista[2]))
    return d


print(Delta())


def X():
    lista = [0.961, -3.666, 3.522]
    delta = Delta()
    x1 = (-(lista[1])+((delta)**(1/2)))/(2*(lista[0]))
    x2 = (-(lista[1])-((delta)**(1/2)))/(2*(lista[0]))
    return x1, x2


print(X())

# valores que entrarão na função
t = np.linspace(1.0, 5.0)


def f(x):
    return  0.426*(4/3 - x/3)*(1.4 - 0.4*x)*(3/2 - x/2)*(2 - x) + 0.714*(2 - x/2)*(2.33333333333333 - 0.666666666666667*x)*(3 - x)*(x - 1) + 0.782*(4 - x)*(7.0 - 2.0*x)*(x/2 - 1/2)*(x - 2) + 0.8168*(8.0 - 2.0*x)*(0.4*x - 0.4)*(0.666666666666667*x - 1.33333333333333)*(2.0*x - 6.0) + 0.874*(x/3 - 1/3)*(x/2 - 1)*(x - 3)*(2.0*x - 7.0)


plt.plot(t, f(t))
plt.grid(True)
plt.show()
