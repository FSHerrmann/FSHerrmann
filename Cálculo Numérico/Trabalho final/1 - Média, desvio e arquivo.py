# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:57:37 2021

@author: feeli
Como o programa parcial já cálculava os valores da forma adequada, importarei
a biblioteca statistics apenas para diminuir o programa, focando na parte que
esteva incompleta. A altura 3.5m será salva como 4, e 4 metros como 5, para
facilitar o código. (no vetor, ocuparão tais locais)
"""
import statistics

f = open("Tempo.txt", "r")
Tempos = [[float(entry) for entry in line.split()] for line in f.readlines()]
f.close()

# Criar a média e o desvio padrão para cada altura as funções "def" estão no
# primeiro programa enviado.

media = []
desvio = []
for x in range(0, 5):
    media.append((statistics.mean(Tempos[x])))
    desvio.append((statistics.pvariance(Tempos[x])))


# Criar arquivo reduzido de forma mais simples:
f = open("Reduzido.txt", "w")
for x in range(0, 5):
    f.write(str(x))
    f.write(" ")
    f.write(str(media[x]))
    f.write(" ")
    f.write(str(desvio[x]))
    f.write("\n")
f.close()
