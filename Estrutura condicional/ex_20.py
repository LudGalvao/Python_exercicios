nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))
nota_3 = float(input("Informa a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
    print(f"Sua média foi {media:.1f} e você foi APROVADO COM DISTINÇÃO")
elif media >= 7:
    print(f"Sua média foi {media:.1f} e você foi APROVADO")
else:
    print(f"Sua média foi {media:.1f} e você foi REPROVADO")