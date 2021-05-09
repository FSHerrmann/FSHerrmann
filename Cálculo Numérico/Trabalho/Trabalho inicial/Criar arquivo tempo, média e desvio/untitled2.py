# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:43:12 2021

@author: feeli
"""

f = open("Tempo.txt", "r")
Tempos = [[float(entry) for entry in line.split()] for line in f.readlines()]
print(Tempos)

