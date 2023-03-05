altura = float(input("Informe a sua altura: "))
sexo = str(input("Informe seu sexo(M ou F): "))

if sexo == "M" or "m":
    peso_homem = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_homem:.1f}kg")

elif sexo == "F" or "f":
    peso_mulher = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_mulher:.1f}kg")

else:
    print("Inválido")