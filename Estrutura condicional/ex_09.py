# Lê os três números
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

# Verifica qual é o maior número
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Verifica qual é o segundo maior número
if (num1 >= num2 and num1 < num3) or (num1 > num3 and num1 < num2):
    segundo_maior = num1
elif (num2 >= num1 and num2 < num3) or (num2 > num3 and num2 < num1):
    segundo_maior = num2
else:
    segundo_maior = num3

# O menor é o que sobrou
menor = num1 + num2 + num3 - maior - segundo_maior

# Imprime os números na ordem decrescente
print(maior)
print(segundo_maior)
print(menor)
