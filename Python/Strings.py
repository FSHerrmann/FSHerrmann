#Strings
#Como definir strings
"""x = 'aaaaa \nbbb \nccc'
print(x)

#Fatiando Strings
x = 'python'
#lista[x:y:z]
#x: Inicio
#Y: Fim
#Z: Passo
print(x[-1])
print(x[1:4:2])
y = 'Todo dia é um bom dia para que está de bem com a vida'
print(y[1:40:3])
print(y[::5])

#Valores das teclas
print( "a" > "X" ) 
print( "a" > "1" ) 
#A tabela ASCII define os valores para as teclas
print(chr(100))
print(ord("d"))

for c in range (123):
    print(str(c) + " - " +  chr(c))
    
    
#Alterando strings
s = "Lista de caracteres"
print(len(s))
print(s)
print(s[6])
# Erro ao tenta direto s[6] = "x"
#Podemos desmontar e então remonta-la
s.split(" ")
lista = s.split(" ")
print(lista)
print(lista[0] + " " + lista[2])

#Podemos sustituir
b = s.replace ("a", "b")
print(b)

c = s.replace("a", "b")
#Toda operação em strings retorna uma nova string
print(id(s))
print(id(b))
print(id(c))"""

#Iterando Strings
#Exemplo 1
s = 'Iterando Strings'
for c  in s:
    print(c)

#Exemplo 2
indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice += 1

print(enumerate((s)))

print(dict(enumerate(s)))  

for k,v in enumerate('Iterando Strings'):
    print(k, v)  






































