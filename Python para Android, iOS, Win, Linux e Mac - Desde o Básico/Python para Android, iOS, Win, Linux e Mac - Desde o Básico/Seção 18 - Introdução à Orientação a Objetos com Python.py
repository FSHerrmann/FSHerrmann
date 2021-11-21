# Aula 118 - Introdução à Orientação a Objetos com Python
# Aula 119 - Primeira Classe
# Aula 120 - Nomeclatura de Classe
# Aula 121 - Criação de Objetos (Instanciação)
# Aula 122 - Membros de Classes
# Class 123 - Constructor Method
# Class 124 - Retangle Class
# Aula 125 - Análise da Declaração de Membros
# Aula 126 - Personalize the consructor method


# Aula 118 - Introdução à Orientação a Objetos com Python
# Da classe criamos objetos, classes são conhecidas também como TAD
# Tipo Abstrato de Dados, exemplo: a classe tel pode armazen. o DDD e o número.
# As regras de orientação de objeto do Python é totalmente diferentes
# das reras de outras linguagens, como Fortran, C++ e Java


# Aula 119 - Primeira Classe
# Herança: Reutiliza um código através da especialização dos objetos
# Composição: Combina expressões e comandos simples em composto.
# Estado: Atributos (variável) referentes as classes
# Comportamento: Funções que manipulam os estados (variáveis)
#
# Estrutura de Hierarquia
#  BaseException
#  SystemExit
#  KeyboardInterrupt
#  GeneratorExit
#  Exception
#    ArithmeticError
#      ZeroDivisionError
#    ImportError
#    NameError
#    ValueError
#
# Características da classe
# Geração de Múltipas Instâncias
# Especialização (Herança/composição)
# Sobrecarga de Operadores
# Polimorfismo
#
#
# Aula 120 - Nomeclatura de Classe
# Não é permitido " ", iniciar com números ou caracteres epeciais.
# Deve ser o estilo CamelCase (Cada palavra inicia Maiúscula)
# Ex: AlunoUfscNovo e não Aluno UFSC novo


# Aula 121 - Criação de Objetos (Instanciação)
# Instância e Objetos são a mesma coisa.
# Classe é o projeto de um objeto
# Objeto é a execução do código de uma Classe
# Instância  é sinônimo de Objeto
# No Python *T*odo Objeto possui um ID composto por um núm. inteiro não negativo
# class Pessoa:
#     pass
# p1 = Pessoa()
# # p1 = None
# p2 = Pessoa()
# print(id(p1))
# print(id(p2))
# print("Bom dia")


# Aula 122 - Membros de Classes
# Propriedades são variáveis que armazenam características (Propiedade == variável)
# Métodos são as funções, as ações que o projeto pode realizar (Método == função)


# Class 123 - Constructor Method
# class A:
#     def __init__(self):
#         print(id(self))
#
#
# a = A()
# print(id(a))


# Class 124 - Retangle Class
# class retangle:
#
#     def __init__(self):
#         self.b = 0
#         self.h = 0
#
#
#     def area(self):
#         return self.b * self.h
#
#
# r1 = retangle()
# r1.b = 10
# r1.h = 5
# print(r1.area())


# Aula 125 - Análise da Declaração de Membros
# Membros podem ser adicionados a objetos de forma interna ou externa a classe
# Quando usandos func() invocamos a função, quando queremos associar a instância ao nome
# apenas func ex:
# def func():
#     pass
# obj.fx = func
# class Retangulo()
#     def area(self):
#         return self.b * self.h
#
#
# def membros_retangulo(r):
#     r.b = 0
#     r.h = 0
#
#
# r1 = Retangulo()
# membros_retangulo(r1)
# r1.b = 10
# r1.h = 5
# print( r1.area() )


# Aula 126 - Personalize the contructor method
# Tem a finalidade de estabelecer os valores obrigatórios
# para construção de um novo objeto
# class Retangulo:
#     def __init__(self, largura, altura):
#         self.l = largura
#         self.a = altura
#
#     def area(self):
#         return self.l * self.a
#
# r = Retangulo(7, 5)
#
# print(r.area())