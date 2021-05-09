#Dicionário: É uma lista especializada onde cada valor está ligado a uma chave
#Ás formas de declarar
'''
{}
print(type({}))

d1 = {}
print(type(d1))

d2 = dict()
print(type(d2))


d1 ['aaa'] = 1000
print(d1)


d3 = dict()
d3 ['001'] = "Camiseta"
d3 ['002'] = "Calça"
d3 ['003'] = "Casaco"
print(d3)

print(d3['002'])

d4 = {1:"Camiseta", 2:"Calça", 3:"Casaco"}
print(d4)

#Funções dos dicionários
#Deletar um elemento
tel = {
       91098945: "Maria",
       91099898: "Felipe",
       91500105: "Simone",
       28349283: "Josué"
          }
print(tel)

print(len(tel))

del(tel[91099898])
print(tel)

#Está função retorna e remove um item
tel = {
       91098945: "Maria",
       91099898: "Felipe",
       91500105: "Simone",
       28349283: "Josué"
          }
print(tel)
print(tel.popitem())
print(tel)
print(tel.popitem())
print(tel)
print(tel.popitem())
print(tel)
print(tel.popitem())
print(tel)
#Caso o dicionario esteja vazio um aviso será dado
print(tel.popitem())
print(tel)
'''
#Operador in e not in
tel = {
       91098945: "Maria",
       91099898: "Felipe",
       91500105: "Simone",
       28349283: "Josué"
          }
print(91099898 in tel)
print(12 in tel)

tel2 = {999999: "teste1", 88888888: "teste2"}
print(tel2)
#Como mesclar dicionários
tel.update(tel2)
print('\n \n ',tel)

#Fazer uma tupla como chave (legal pra Cripto)
t = (10,10,10)
tel[t] = "AcessoConcedido"
print('\n\n\n', tel, '\n\n')
#Não posso usar listas
l = [1,2,3]
tel[l] = 5
print(tel[l])














