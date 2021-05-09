# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:39:49 2021

@author: feeli
"""

#Função Aninhada
def func():
    print("func")
    
    def func_interna():
        print("func_interna")
        
    func_interna()

func()