lado_1 = float(input("Informe o primeiro lado do triangulo: "))
lado_2 = float(input("Informe o segundo lado do triangulo: "))
lado_3 = float(input("informe o terceiro lado do triangulo: "))

if lado_1 + lado_2 < lado_3:
    print("Não forma um triangulo")

elif lado_1 == lado_2 and lado_2 == lado_3:
    print("Triangulo Equilátero")

elif lado_1 != lado_2 and lado_2 != lado_3:
    print("Triangulo Escaleno")

else:
    print("Triangulo isósceles")
    