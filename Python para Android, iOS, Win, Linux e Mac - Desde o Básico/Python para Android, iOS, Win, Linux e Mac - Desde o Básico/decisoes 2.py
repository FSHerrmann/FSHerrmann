numero1 = int(input("Entre com o primeiro valor "))
numero2 = int(input("Entre com o segundo valor "))

if (numero1 == numero2):
    print("Valores iguais")
if (numero1 < numero2):
    print("O numero %d e menor que %d"%(numero1,numero2))
if (numero1 > numero2):
    print("O numero %d e maior que %d"%(numero1,numero2))

print(type(numero1))
print(type(numero2))

print("O valor de %d elevado a %d sera: "%(numero1,numero2),(numero1**numero2))
