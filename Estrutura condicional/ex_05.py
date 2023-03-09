nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media == 10.0:
    print(f'Sua média foi {media} e você foi aprovado com Distinção!')
elif media >= 7.0:
    print(f'Sua média foi {media} e você foi aprovado!')
else:
    print(f'Sua média foi {media} e você foi reprovado.')
    