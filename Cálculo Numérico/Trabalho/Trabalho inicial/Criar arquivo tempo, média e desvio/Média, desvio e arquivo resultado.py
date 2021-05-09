# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:32:11 2021

@author: Felipe Schneider Herrmann

Programa desenvolvido para a matéria de cálculo numérirco.

"""
# Lê o arquivo, e salvar em vetor, favor alterar o local, conforme
# salvou o arquivo "Tempo.txt"

f = open("Tempo.txt", "r")
vetor = [[float(entry) for entry in line.split()] for line in f.readlines()]


def vmedio():
    for x in (0, 4):
        print(vetor)


media = vmedio()


def dpadrao():
    soma = 0
    for i in range(0, 5):
        soma += ((vetor[i] - media)**2)
    soma = (soma/4)
    return((((soma))**(1/2)))


desvio = dpadrao()

print("vetor: ", vetor, "\nmédia: ", media, "\ndesvio: ", desvio)


# Modificar arquivos e salvar
mediastr = str(media)
desviostr = str(desvio)

with open("Resultados.txt", 'w') as f:
    f.write("Tempos: ")
    for item in vetor:
        f.write("%s, " % item)
    f.write("\nMedia: ")
    f.write(mediastr)
    f.write("\ndesvio:")
    f.write(desviostr)
