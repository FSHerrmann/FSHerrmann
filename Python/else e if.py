numero1 = input("Entre com um numero ")
print(type(numero1))

numero1 = (int(numero1))
print(type(numero1))
# ou
numeroj = int(input("Entre com um numero "))
print(type(numeroj))

if (type(numero1)==type(numeroj)):
    print("Dois numeros!")
    
if (numero1==numeroj):
    print("Numeros iguais ")
else: print("Numeros diferentes ")