pre_1 = float(input('Informe o preço do primeiro produto: '))
pre_2 = float(input('Inforem o preço do segundo produto: '))
pre_3 = float(input('Informe o preço do terceiro produto: '))

if pre_2 > pre_1 and pre_3 > pre_1:
    print(f'O produto mais barato é o produto 1 custando R$ {pre_1:.2f}')
elif pre_1 > pre_2 and pre_3 > pre_2:
    print(f'O produto mais barato é o produto 2 custando R$ {pre_2:.2f}')
else:
    print(f'O produto mais barato é o produto 3 custando R$ {pre_3:.2f}')

