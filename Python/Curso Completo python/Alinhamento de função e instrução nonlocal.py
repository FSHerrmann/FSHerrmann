# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:39:49 2021

@author: feeli
"""

#Função Aninhada
# def func():
#     print("func")
    
#     def func_interna():
#         print("func_interna")
        
#     func_interna()

# func()

#Nonlocal acessa membros externos

def func():
    
    var_local = 10
    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)
    func_interna()

func()

#Não funciona globalmentem apenas em funções externas
# x = 10
# def funx():
#     nonlocal x
#     print(x)

# funx()
    
#Para acessar variáveis globais usa-se o comando global
x1 = 32
def funx1():
    global x1
    print(x1)

funx1()
    
