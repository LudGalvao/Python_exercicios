numero = float(input("Informe um número: "))

if numero == round(numero): # arredonda o valor
    print(f"{numero} é um número inteiro")
else:
    print(f"{numero} é um número decimal")