nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Infoerme a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media >= 9.0:
    print('Conceito A')
    print('Aprovado')
elif media >= 7.5:
    print('Conceito B')
    print('Aprovado')
elif media >= 6.0:
    print('Conceito C')
    print('Aprovado')
elif media >= 4.0:
    print('Conceito D')
    print('Reprovado')
else:
    print('Conceito E')
    print('Reprovado')
