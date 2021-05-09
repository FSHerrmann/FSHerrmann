# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:27:06 2021

@author: feeli

"""
# Boa parte achei neste link:

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


# Vou fazer a liearização dos pontos, usei como referência a página:
# https://sites.google.com/site/cnumer3q16/atividade4?tmpl=%2Fsystem%2Fapp%2Ftemplates%2Fprint%2F&showPrintDialog=1
def Lagrange(z, xn):
    lista = [1, 2, 3, 3.5, 4]
    y = [0.426, 0.714, 0.782, 0.8168, 0.874]
    xf = xn+z
    xu = xn
    p = 0
    for j in range(xu, xf):
        resultado = 1
        for i in range(xu, xf):
            if (xn != i):
                resultado = resultado*((x-lista[i])/(lista[xn]-lista[i]))
        print(resultado)
        p = p+(resultado*(y[j]))
        xn = xn + 1
    print(p)


def Gravidade(z, xn):
    lista = [1, 2, 3, 3.5, 4]
    y = [0.45152, 0.63855, 0.78206, 0.84472, 0.90304]
    xf = xn+z
    xu = xn
    p = 0
    for j in range(xu, xf):
        resultado = 1
        for i in range(xu, xf):
            if (xn != i):
                resultado = resultado*((x-lista[i])/(lista[xn]-lista[i]))
        print(resultado)
        p = p+(resultado*(y[j]))
        xn = xn + 1
    print(p)



# Imprimir quantidade de L's
print(Lagrange(3, 0))
print(Gravidade(3, 0))


# Expandir a equação:
p = 0.426*(3/2 - x/2)*(2 - x) + 0.714*(3 - x)*(x - 1) + 0.782*(x/2 - 1/2)*(x - 2)
sympy.expand(p)
q = 0.45152*(3/2 - x/2)*(2 - x) + 0.63855*(3 - x)*(x - 1) + 0.78206*(x/2 - 1/2)*(x - 2)
sympy.expand(q)

# Cálculo das raízes:
def Delta():
    lista = [0.961, -3.666, 3.522]
    d = ((lista[1])**(2))-(4*(lista[0])*(lista[2]))
    return d


def Delta2():
    lista = [-0.02176, 0.25231, 0.22097]
    d = ((lista[1])**(2))-(4*(lista[0])*(lista[2]))
    return d

print(Delta())
print(Delta2())


def X():
    lista = [0.961, -3.666, 3.522]
    delta = Delta()
    x1 = (-(lista[1])+((delta)**(1/2)))/(2*(lista[0]))
    x2 = (-(lista[1])-((delta)**(1/2)))/(2*(lista[0]))
    return x1, x2

def Y():
    lista = [-0.02176, 0.25231, 0.22097]
    delta = Delta()
    y1 = (-(lista[1])+((delta)**(1/2)))/(2*(lista[0]))
    y2 = (-(lista[1])-((delta)**(1/2)))/(2*(lista[0]))
    return y1, y2

# print()

print (X())
print (Y())
# Tamanho do gráfico
t = np.linspace(0.4, 4.5)


def f(x):
    return 0.426*(4/3 - x/3)*(1.4 - 0.4*x)*(3/2 - x/2)*(2 - x) + 0.714*(2 - x/2)*(2.33333333333333 - 0.666666666666667*x)*(3 - x)*(x - 1) + 0.782*(4 - x)*(7.0 - 2.0*x)*(x/2 - 1/2)*(x - 2) + 0.8168*(8.0 - 2.0*x)*(0.4*x - 0.4)*(0.666666666666667*x - 1.33333333333333)*(2.0*x - 6.0) + 0.874*(x/3 - 1/3)*(x/2 - 1)*(x - 3)*(2.0*x - 7.0)


def g(y):
    return 0.45152*(4/3 - y/3)*(1.4 - 0.4*y)*(3/2 - y/2)*(2 - y) + 0.63855*(2 - y/2)*(2.33333333333333 - 0.666666666666667*y)*(3 - y)*(y - 1) + 0.78206*(4 - y)*(7.0 - 2.0*y)*(y/2 - 1/2)*(y - 2) + 0.84472*(8.0 - 2.0*y)*(0.4*y - 0.4)*(0.666666666666667*y - 1.33333333333333)*(2.0*y - 6.0) + 0.90304*(y/3 - 1/3)*(y/2 - 1)*(y - 3)*(2.0*y - 7.0)


plt.plot(t, g(t), label = "Gravidade = 9.81 m/s²")
plt.plot(t, f(t), label = "Gravidade =" )
plt.grid(True)
plt.xlabel('Altura (m)')
plt.ylabel('Tempo (s)')
plt.legend(loc='upper left')
plt.show()
