# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:27:39 2021

@author: feeli

Essa era a parte que faltava no trabalho inicial, portanto irem deixar um
pouco menos enxuto
"""

import matplotlib.pyplot as plt
import numpy as np

# Abrir, ler o arquivo Reduzido e fecha-lo
f = open("Reduzido.txt", "r")
valores = [[float(entry) for entry in line.split()] for line in f.readlines()]
f.close()

print("Os valores recebidos do arquivo são: \n", valores, "\n")

# Arrumando as alturas
valores[0][0] = 1
valores[1][0] = 2
valores[2][0] = 3
valores[3][0] = (3.5)
valores[4][0] = 4
print("Os valores, conforme pedidos são: ", valores, "\n")


# Simulando a gravidade (conforme trabalho inicial)
def gravidade():
    variavelx = []
    variavely = []
    for x in np.arange(0.5, 5, 1):
        variavelx.append(x)
        a = (((2*x)/(9.81))**(1/2))
        variavely.append(a)
    return(variavelx, variavely)


gravidadex, gravidadey = gravidade()

# Criando o gráfico
plt.plot(gravidadex, gravidadey)
plt.xlabel('Altura (m)')
plt.ylabel('Tempo (s)')
for x in range(0, 5):
    plt.plot(valores[x][0], valores[x][1], "ro")

# Tive problemas ao salvar o gráfico, consegui corrigi-lo "salvando", antes
# de plotar.
graph = plt.gcf()
plt.show()

# Salvando o gráfico

graph.savefig("TGrafico inicial.png")
