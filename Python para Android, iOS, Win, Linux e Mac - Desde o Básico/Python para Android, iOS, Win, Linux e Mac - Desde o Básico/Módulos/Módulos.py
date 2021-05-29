# Para esta parte, foi criado o arquivo Estudos.py, que posteriormente
# foi renomeado como AuxiliarModulos.py

# 100 Introdução aos Módulos
# Um módulo é um arquivo contendo definições e comandos em Python para serem usados em outros programas em Python.
# A Biblioteca é um conjunto de módulos.
# São usados para evitar DRY (Don't Repeat Yourself)
# Funções elementares: Reutilização de código, Namespace, Compartilhamento de estrutura de dados.


# 101 Escopo e Tabela de Símbolos
# Escopo e tabela de símbolos.
# def func():
#     print(__name__)
# func()
# a = 0
# print(vari)
# la = list()
# for x in [1, 2]:
#     b = 0
# Usando debugger e alt+f8 posso ver todas funções, sejam buildings ou declaradas.


# # 102 Importando módulos
# # Importar "módulo" pelo "nome"
# import math
# # Sempre que uma variável, como euler for invocada, o seu valor será procurando dentro da biblioteca, portanto, uma
# # boa prática de programação, é salvar o valor em uma variável.
# e = math.e
# pi = math.pi
# # Usando debug + altF8 é possível ver que o nome do módulo é importado, e todos os módulos que ele possui (dir(math))
# print(e)
# print(pi)


# # 103 Importação de Símbolos
# from math import e
# print(e)
# # Posso deletar o símbolo ou biblioteca.
# del e
# # print(e)
# # Posso importar mais de um símbolo por vez
# from math import e, pi, sqrt  # Square
# # Sqrt é uma função e não uma variável.
# print("Importando 3 símbolos: ", sqrt(e**pi))
# # Também se for importar math e, individualmente, atribuir valores, como: e = math.e, porém o código ficará maior.
# def func():
#     from math import factorial
#     print("factorial", factorial(10))
# func()
# del e, pi, sqrt
# # Outra forma de importar, más não recomendada, pela demora é usando *, assim todos símbolos
# # deverão ser importados, porém a tabela ficara desorganizada e as aplicações ficarão mais lentas.
# from math import *
# # Visualizando as variáveis globais, é possível ver a confusão causada.


# 104 Crianção de módulos
# Módulo Main, ligado ao módulo AuxiliarModulos.py
# Para importar, preciso marcar a pasta como
# "source root"
# from AuxiliarModulos import *
# print(a)
# print(b)
# f()
# print(__name__)


# 105 Localização de módulos
# Diretório Base: Onde foi executado, não recomendado
# Diretório Variável: PYTHONPATH
# Diretório da biblioteca padrão.
# Diretório definidos por arquivos *.pth
# Ordem de procura
# Módulo.pyd(*.dll no windows ou *.so no Unix)
# Módulo.py
# Módulo.pyc ou .pyo (gerados no modo de optimização).
# Módulo(pasta)
# modulo.so (em Linux)
# Uma imagem da memória
# from pprint import pprint
# import sys
# pprint(sys.path)
# import AuxiliarModulos
# Para adicionar basta colocar sys.path.insert(0 , "C:\\...)
# Cada módulo só pode ser importado uma vez.
# from sys import path as lpath#
# pprint(lpath)
# Onde o Pycharm procura
# 'C:\\Users\\feeli\\Documents\\Python para Android, iOS, Win, Linux e Mac - '
#  'Desde o Básico\\Módulo',
#  'C:\\Users\\feeli\\Documents\\Python para Android, iOS, Win, Linux e Mac - '
#  'Desde o Básico\\Módulo',
# Onde o Python procura
#  'C:\\ProgramData\\Anaconda3\\python38.zip',
#  'C:\\ProgramData\\Anaconda3\\DLLs',
#  'C:\\ProgramData\\Anaconda3\\lib',
#  'C:\\ProgramData\\Anaconda3',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin']


# 106 Importação do módulo
# Localização, Compilação(pyc) e Execução.
# Verificar bitcode da função (mais rápido que executar a função em sí)
# import dis
# def func(l):
#     print("O que temos nessa função?")
# dis.dis(func)
# Para os arquivos importados é criado um pycash


# # 107 Símbolos privados
# # Variáveis com _ não são importados, são apenas locais.
# from AuxiliarModulos import *
# from pprint import pprint
# pprint(globals())
# print(soma)
# # Apesar de não serem importados automaticamente, os
# # símbolos podem ser importados de forma individual
# from AuxiliarModulos import _a
# pprint(globals())
# print(_a)


# # 108 Símbolos Públicos
# from AuxiliarModulos import *
# # Evitar importar desta forma, pois são importados
# # muitos símbolos, más posso definir quais deles virão, alterando
# # o arquivo em sí.
# from pprint import pprint
# pprint(globals())


# 109 Módulo Principal
# Será o primeiro arquivo de script(?) em python a ser executado
# receberá o nome __main__, também é conhecido como arquivo de
# nível superior.
# if __name__ == "__main__":
#     print("Este é o módulo superior")
# A Nomenclatura segue a mesma regra que varáveis e funções.
# o arquivo main não precisa ter a extensão .py, os outros sim, ou
# uma linguagem reconhecida pelo python.
# Importar algo com nome reservado na linguagem acarreta em erro.

# 110 Recarregamento de módulos
# Sempre que for recarregado, seus membros serão perdidos.
# Este recurso deve ser utilizado com cautela, pois geralmente
# reimportamos por consequência de más práticas de programação
# import importlib
# from AuxiliarModulos import a, b
# print(a*b)
# importlib.reload(AuxiliarModulos)
# print(a)

