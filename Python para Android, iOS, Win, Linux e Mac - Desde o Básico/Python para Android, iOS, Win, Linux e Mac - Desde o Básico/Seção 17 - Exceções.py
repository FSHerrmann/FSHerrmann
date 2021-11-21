# Seção 17
# Aula 111 - Introdução as exceções
# Aula 112  - Valores Inválidos --> Tentar Pedir o valor 0 novamente <--
# Aula 113 - Tratamento de Exceções Multíplas I
# Aula 114 - Tratamento de Exceções Multíplas II
# Aula 115 - Capturando a instância do erro
# Aula 116 - Bloco Else
# Aula 117 - Bloco Finally


# Aula 111 - Introdução as exceções
# Exceções servem quando se pode prever possíveis erros, implementando suas
# soluções, ou apenas permitindo ao proramador estar ciente das mesmas
# Devemos evitar um código que levante uma exceção, devemos tentar resolver o
# erro, a simples premissa de uma maior necessidade
# do uso computacional, já valida o não uso das exceções.
# a = (10 / 0)
# #try:
#     a = (10 / 0)
#     print(a)
# except ZeroDivisionError:
#     print("Não é possível dividr por zero")


# Aula 112  - Valores Inválidos --> Tentar Pedir o valor 0 novamente <--
# def input_float(msg):
#     while True:
#         try:
#             return float(input(msg))
#         except ValueError:  # Em caso de letra e não número
#             print("Número inválido.")


# num1 = input_float("Digite o primeiro numero: ")
# num2 = input_float("Digite o segundo numero: ")

# try:
#     print(num1 / num2)
# except ZeroDivisionError:  # Em caso de dividir por zero
#     print("Não é possível dividir por zero.")


# Aula 113 - Tratamento de Exceções Multíplas I
# Um código pode ter várias exceções, aqui será estudada a forma de resolver
# tais exceções.

# def erro(x):
#     try:
#         eval(x)  # Função que "interpreta" aquilo que acontece
#     except TypeError:
#         print("TypeError")
#     except NameError:
#         print("NameError")
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     except ValueError:
#         print("ValueError")


# # TypeError
# erro("int+int")
# # NameError
# erro("num1")
# # ZeroDivisionError
# erro("1/0")
# # ValueError
# erro("int('a')")

# print("A aplicação foi finalizada")


# Aula 114 - Tratamento de Exceções Multíplas II
# Uma reprodução da Aula 113, podem com o mesmo tratamento para dois erros.

# def erro(x):
#     try:
#         eval(x)
#     except(TypeError, NameError):
#         print("NameError ou TypeError")


# # TypeError
# erro("int+int")
# # NameError
# erro("a")


# Aula 115 - Capturando a instância do erro
# def erro(x):
#     try:
#         eval(x)
#     except ValueError as e:
#         print("ValueError")
#         print(type(e))  # Instância da exceção
#         print(e.args)  # Argumentos as mensagens
#         print(e)  # _str_mensagem
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     except (TypeError, NameError) as e:  # Pode ser chamado de e também
#         # Pois apenas um erro é identificado usado.
#         print("NameError ou TypeError")
#         print(type(e))  # Instância da exceção
#         print(e.args)  # Argumentos as mensagens
#         print(e)  # _str_mensagem


# # ValueError
# erro("int('a')")
# # TypeError
# erro("int+int")
# # NameError
# erro("a")


# Aula 116 - Bloco Else
# Adiciona um else ao final
# def erro(x):
#     try:
#         eval(x)
#     except TypeError:
#         print("TypeError")
#     else:
#         print("Nenhum erro ocorreu")


# erro("10+10")
# erro("int+int")
# print("A aplicação foi finalizada")


# Aula 117 - Bloco Finally
# Bloco que sempre será executado e
# iremos fechar arquivos ou conexões de rede em andamento

# def erro(x):
#     try:
#         eval(x)  # Função que "interpreta" aquilo que acontece
#     except NameError:
#         print("NameError")
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     except ValueError:
#         print("ValueError")
#     else:
#         print("Else")
#     finally:  # Sempre será executado
#         print("Finally foi executado")


# # NameError
# erro("num1")
# # ZeroDivisionError
# erro("1/0")
# # ValueError
# erro("int('a')")
# # Else
# erro("int('2')")

# print("A aplicação foi finalizada")