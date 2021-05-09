# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:49:41 2021

@author: feeli
"""
import matplotlib.pyplot as plt
import numpy as np

f = open("Reduzido.txt", "r")
tempos = f.readlines()
print(tempos)

# converter o vetor


def converter():
    for i in tempos:
        vetor = []
        for x in range(0, 5):
            vetor.append(i.split(',')[x])
            f.close()

    vetor = list(map(float, vetor))
    return(vetor)


tempos = converter()
print(tempos)


tempos = list(map(float, tempos))
print(tempos)



alturas = [1, 2, 3, 3.5, 4]


# Criando o gráfico da gravidade no eixo x e y
def gravidade():
    variavelx = []
    variavely = []
    for x in np.arange(0.5, 5, 1):
        variavelx.append(x)
        a = (((2*x)/(9.81))**(1/2))
        variavely.append(a)
    return(variavelx, variavely)


gravidadex, gravidadey = gravidade()




plt.grid(True)
plt.plot(gravidadex, gravidadey)
plt.scatter(alturas, tempos, color = 'r', linestyle = ":")
plt.xlabel('Altura (m)')
plt.ylabel('Tempo (s)')


plt.show()

plt.savefig('gráfico.png')
