# coding: utf-8
# Sempre definir o encoding.
# MÓDULO de estudo
# def f():
#     for x in range(0, 4):
#         print("f", x)
#
#
# a = 10
# b = "Modulo personalizado"
#
# # O Módulo é acessado e interpretado, de forma que
# # todas linhas sejam executadas.
# print("Módulo executado")
# print(__name__)

# 107
# Usar _ é dizer que é uma variável de uso local.
# Por tanto, não devem ser importada
# _a = 10
# _b = 20
# _c = 30
# soma = _a + _b + _c

# 108
# # Como definir quais variáveis importar.
# __all__ = ["aa", "ab"]
# # Estes serão importados
# aa = 0
# ab = 1
# # Estes não
# ba = 2
# bb = 3

# 109
# if __name__ == "__name__":
#     print("Sim, este é o main")
# elif __name__ != "__name__":
#     print("Não é o main")

# 110
# a = 2
# b = 3
# c = 4