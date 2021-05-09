# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:51:52 2021

@author: feeli
Lê os arquivos como em 2,  manipula Usando as funções em 3, e gera o
gráfico linearizado.
"""
import importlib
import matplotlib.pyplot as plt
import numpy as np

# import Linearizações

# Ctrl C + Ctrl V
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
    




plt.show()
