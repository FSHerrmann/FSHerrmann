#Funções: Agrupamento de um conjunto de ações, evitar usar variaveis globais
#Permite que seja mais fácil verificar problemas, justamente pelas variaveis serem locais
#Função é um bloco de instrução independente
#Função vs Método: Metodo não retorna um valor

#Definidindo funções
"""def minha_func():
    print("Bom dia")


#Parametros de funções
#Argumento:Invocando a função e parametros:Na definição da função
print()

def soma(x,y):
    total = x + y
    print("o Total da soma x + y será: ",total)

soma(10, 50)

#Parametros Default: Parametros fixos.
def login(usuário = "Root", senha = "123"):
    print("Usuário:", usuário)
    print("Senha: ", senha)

#Alterando os parametros iniciais
login("Claudio","312")

#Em exatas, posso fazer a função com todo o cálculo complexo e escolher os valores
def quadrado(x = 2):
    print(x**2)

quadrado()
quadrado(3)
quadrado(12)



#Argumentos posicionais e nomeados
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))
    
dados_pessoais("Felipe", "Schneider", 27, True) 

# Parametros podem ser enviado de forma diferente
 dados_pessoais(sexo=True,
                 nome="Claudio", 
                 idade=30, 
                 sobrenome="Carvalho")

def mult(x,y):
    num = x * y
    return num
    #Tudo que vier depois não será executado    

print(mult(10,10))

print(mult)
    
#Retorno de multiplos valores
def func():
    return 1, 2

#a, b = 10, 20
#a , b = func()
a, b = func()

print(a)
print(b)

def potencia(x):
    quadrado  = x**2
    cubo = x**3
    
    return (quadrado, cubo)

print(potencia(5))

a ,b = potencia(10)
print(a,b)


def lista_de_argumentos(*lista):
    print(lista)

def lista_de_argumentos_associativos(**dicionario):
    print(dicionario)


lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos("um","dois","três","quatro")

lista_de_argumentos_associativos(a=1, b=2, c=3, d=4)
lista_de_argumentos_associativos(um=1,dois=2,tres=3,quatro=4)
"""
  

# #Empacotamento
# #lista = [10,20]
# #Desempacotamento é a extração dos elementos contidos em uma estrutura 
#usando *(lista) ou **(dicionário)
# lista = [10, 20]
# def func(a ,b):
#     print()
#     
# func(*lista)
# func(10, 20)
# func(a=10, b=20)
# 
# def pessoa(Nome, Sobrenome, Idade):
#     print(Nome)
#     print(Sobrenome)
#     print(Idade)
#     
# #lista = "Felipe", "Schneider", 27
# 
# #pessoa(tupla[0], tupla[1], tupla[2])
# 
# #Usando desempacotamento
# #pessoa(*lista)
# 
# d = {"Nome":"Felipe","Sobrenome":"Schneider","Idade":27}
# pessoa(**d)
# 
# =============================================================================

#Dempacotamento 2 
lista = [110 , -10, 12**3]

def func(a, b, c):
    print(a)
    print(b)
    print(c)
    
    
# func(*lista)
# lista.sort()
# func(*lista)

#Como tuplas são imutaveis, o sort não funciona,então transformaremos em lista a depois 
# ordenaremos

# tupla = 11, 10, 12
# l = [*tupla]
# l.sort()
# func(*l)

#ZIP e dict 
z = zip(("a","b","c"),(1,2,3))
# print(z)

# print(dict(z))

func(**dict(zip(("b", "a", "c"),lista)))











































  