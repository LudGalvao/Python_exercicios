numero = float(input("Informe um número: "))
operacao = int(input("Escolha um(1 - par/impar, 2 - positivo ou negativo, 3 - inteiro ou decimal): "))

if operacao == 1:
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é impar")

elif operacao == 2:
    if numero < 0:
        print(f"O número {numero} é negativo")
    else:
        print(f"O número {numero} é positivo")

elif operacao == 3:
    if numero == round(numero): # arredonda o valor
        print(f"{numero} é um número inteiro")
    else:
        print(f"{numero} é um número decimal")

else:
    print("Escolha inválida")