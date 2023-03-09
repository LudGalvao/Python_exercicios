salario = float(input('Informe o seu sálario R$: '))

if salario <= 280:
    calc = (salario * 20) / 100
    print(f'Seu sálario atual é R${salario:.2f}')
    print(f'O reajuste foi de 20%')
    print(f'O seu sálario com o aumento de 20% ficou R${calc + salario:.2f}')

elif 280 <= salario < 700:
    calc = (salario * 15) / 100
    print(f'Seu sálario atual é R${salario:.2f}')
    print(f'O reajuste foi de 15%')
    print(f'O seu sálario com o aumento de 15% ficou R${calc + salario:.2f}')

elif 700 <= salario < 1500:
    calc = (salario * 10) / 100
    print(f'Seu sálario atual é R${salario:.2f}')
    print(f'O reajuste foi de 10%')
    print(f'O seu sálario com o aumento de 10% ficou R${calc + salario:.2f}')

else:
    calc = (salario * 5) / 100
    print(f'Seu sálario atual é R${salario:.2f}')
    print(f'O reajuste foi de 5%')
    print(f'O seu sálario com o aumento de 5% ficou R${calc + salario:.2f}')
