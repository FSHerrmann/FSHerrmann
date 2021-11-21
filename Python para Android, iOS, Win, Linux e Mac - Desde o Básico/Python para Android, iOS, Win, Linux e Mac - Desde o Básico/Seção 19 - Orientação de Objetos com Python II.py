# Aula 127 - Encapsulamento
# Aula 128 - Métodos Assessores - Getters e Setters
# Aula 129 - Visibilidade de membros
# Aula 130 - Propriedades I

# Aula 127 - Encapsulamento
# É o isolamento do código
# Interface Pública é o conjunto de métodos públicos para
# acssar os recursos e funcionalidade do código encapsulado
# class Retangulo:
#
#     def __init__(self, largura, altura):
#         self.l = largura
#         self.a = altura
#
#     def area(self):
#         return self.l * self.a
#
#
# r = Retangulo(10, 5)
# r.l = "teste  " # Não é garantido qual o tipo do objeto
# # Logo, ele fez 5 * "teste  "
# print(r.area())

# Aula - 128 Métodos Assessores - Getters e Setters
# São métodos utilizados na contrução da Interface Pública (Interface de Acesso)
# Métodos Getters: sempre retornam valores Get significa o retorno de dados
# Métodos Setters: sempre recebem valores por parâmetros
# Métodos Assessores também garantem a integridade das informações internas ao objeto

# "get_" + "atributo" ou get_atributo
# get_atributo()
# "set_" + "atributo" ou get_atributo
# get_idade()
# set_idade(valor)

# print(isinstance("1",int)) # Verifica se o valor passado é igual ao segundo parâmetro.
# print(isinstance(1,int))
#
# class Retangulo:
#
#     def __init__(self, largura, altura):
#         self.largura = 0
#         self.altura = 0
#         self.set_altura(altura)
#         self.set_largura(largura)
#
#     def set_altura(self, num):
#         if(not(isinstance(num, int) and (num > 0))):
#             raise ValueError("Altura é inválida: {}".format(num))
#         self.altura = num
#
#     def set_largura(self, num):
#         if(not(isinstance(num, int) and (num > 0))):
#             raise ValueError("Largura é inválida: {}".format(num))
#         self.largura = num
#
#     def get_area(self):
#         return self.altura * self.largura
#
# # r = Retangulo(largura = 10, altura = 5)
# # r = Retangulo(altura = 1, largura = -1)
# r = Retangulo(altura = 1, largura = "Teste")


# Aula 129 - Visibilidade dos Membros
# É um recurso da orientação objetos que impede o acesso externo a membros
# de uso exclusivamente interno ao objeto
# A ocultação de membros não ocorre na prática, o Python não possui este recurso
# Convenção da linguagem: Membros de uso exclusivamente interno ao objeto deverão
# ter seus nomes procedidos por UM underline
# publico = 0
# _restrito = 0

# class Pessoa:
#     def __init__(self):
#         self._attr =  0
#     def _func(self):
#         pass

# Colisão de nomes
# Para evitar a colisão de nomes entre a superclasse e a subclasse
# o membro deve ser procedido por DOIS underlines
# __colisao = 0

# class Pessoa:
#     def __init__(self):
#         self._attr = 0
#         _Pessoa__attr # Fora do escopo o nome será este
# Método mágicos
# são precedidos e finalizados com DOIS underlines
# (dunders) e são exclusivos da linguagem, dunders = __
#
# class Retangulo:
#     def __init__(self, largura, altura):
#         self._largura = 0
#         self._altura = 0
#         self.__var = 0
#         self.set_altura(altura)
#         self.set_largura(largura)
#     def set_altura(self, num):
#         if (not(isinstance(num, int)and(num > 0))):
#             raise ValueError("Altura é inválida: {}".format(num))
#         self._altura = num
#         self.__var = 456
#     def set_largura(self, num):
#         if(not(isinstance(num, int) and (num > 0))):
#             raise ValueError("Largura é inválida: {}".format(num))
#         self._largura = num
#     def get_area(self):
#         return self._altura * self._largura
#
#
# r = Retangulo (largura = 5, altura = 5)
# r = Retangulo (largura = 5, altura = 5)
# print(r)

# Aula 130 - Propriedades I
# É um recurso para declaração de membros públicos
# que permite invocar métodos na leitura e escrita de valores
# ecrita:
# instancia.attr = 0
# leitura:
# x = instancia.attr

class A:
    def __init__(self):
        self._var = 0
    def _get_var(self):
        print("O valor está sendo lido")
        return self._var
    def _set_var(self, x):
        print("O valor está sendo escrito")
        self._var = x

        var = property(fget=_get_var, fset=_set_var) # ** forma mais eficiente


a = A() #**
a.var = 10#**
print(a.var)#**
# a.set_var(1000)
# print(a.get_var())