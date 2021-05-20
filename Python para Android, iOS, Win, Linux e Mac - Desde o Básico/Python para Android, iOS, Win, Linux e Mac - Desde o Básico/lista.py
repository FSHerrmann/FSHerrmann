''''Aterar uma lista usando um tamanho estático
lista_nums = [100,200,300,400]
for item in range(4):
    lista_nums[item] += 1000
print(lista_nums)

Alterar uma lista usando um tamanho dinâmico
lista_nums = [100,200,300,400,-200,32,-304]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)


Função Enumerate
lista_nums = [100,200,300,400,-200,32,-304]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)
'''
