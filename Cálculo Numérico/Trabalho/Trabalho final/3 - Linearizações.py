# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:27:06 2021

@author: feeli
Essa parte do programa servida para criar a funções de linearização, sua
aplicação e a crianção do gráfico final se dará em outro programa.
"""
import numpy as np
import matplotlib.pyplot as plt


def diferenca(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for i in range(1, n):
        for j in range(n - i):
            coef[i][j] = \
            ((coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i]))
    return(coef)


def newton(coef, x, y):
    n = len(x)-1
    w = 0
    p = coef[n]
    for w in range(1, w+1):
        p = coef[n-w] + (x-y[n-w])*p
    return p

