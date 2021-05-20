# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:21:29 2021

@author: feeli
"""

lista = [11, 10, 12]


def func(a, b, c):
    print(a)
    print(b)
    print(c)
    
# lista.sort()
# func(*lista)

# tupla = 11, 10, 12 #Imutavel

# l = [*tupla] #Tupla vira lista

# l.sort()
# print(func(*l))

# zip(("a", "b", "c"),(1, 2, 3))

# z = zip(("a", "b", "c"),(1, 2, 3))
# print(z)

# print(dict(z))

print(func(**dict(zip(("b", "a", "c"), lista))))