'''lista = "Bom-dia, vamos praticar Python"
print(lista[::2])

l = ["bbb","ccc","ddd"]
print (l)

l.append("eeee")
print(l)

l.insert(0,"aaa")
print(l)

l.clear()
print(l)

l = ["aaa","bbb","ccc","ddd"]
l.pop(1)
print(l)


l = ["aaa","bbb","ccc","ddd"]
del(l[1:3])
print(l)


l = ["aaa","bbb","ccc","ddd"]
del(l[::2])
print(l)

lista = ["Avião", "Bola", "Cachorro", "Drogas", "Estudos", "Felipe"]
print(lista)

lista.reverse()
print(lista)
lista.reverse()
print(lista)

print(lista.reverse()) #erro#


lista = [1, 27, 143, 92, 9, 0]
lista.sort() 
print(lista)

lista.sort(reverse=True)
print(lista)

lista = ["Avião", "Bola", "Cachorro", "Drogas", "Estudos", "Felipe"]
print(len(lista))

print(lista[len(lista)-1])

#Verificar se está repetido
lista = ["Avião", "Bola", "Cachorro", "Drogas", "Estudos", "Felipe"]
lista.insert(5, "Bola")
print(lista)

lista.append("Bola")


print(lista)
print(lista.count("Bola"))
print(lista.count("Cachorro"))

#Achar o indice
print(lista.index("Cachorro"))
print(lista.index("Bola"))

# Tuplas
t = ("aaa",1,True)
print(t)
print(type(t))

#Operador In e Out
a = (1,2,3,4,5,6,8,9,0,6,7,8,2,3)
b = 1 in a
print(b)
b = 1 not in a
print(b)
b = (0 in range (1,4,2))
print(b)
if 3 in a:
    print("Contido")
else:
        ("Não contido")
'''
a = 10
b = 25
c = 66

x = int(input("Digite um número: "))

if (x == a or x == b or x == c):
    print("Está contido")
else:
    print("Não está contido")









































