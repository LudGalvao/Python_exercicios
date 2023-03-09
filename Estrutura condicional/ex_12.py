hora = int(input('Informe quantas horas você trabalha anualmente: '))
valor_hora = float(input('Informe o valor da hora R$: '))
salario = valor_hora * hora

if salario <= 900:
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    print(f'Seu desconto do inss é R${inss:.2f}')
    print(f'Seu desconto do fgts é R${fgts:.2f}')
    print(f'Total de desconto: {inss:.2f}')
    print(f'O seu sálario liquido é {salario - inss:.2f}')

elif 900 < salario <= 1500:
    ir = (salario * 5) / 100
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    print(f'Seu sálario bruto é R${salario:.2f}')
    print(f'Seu desconto do ir é R${ir:.2f}')
    print(f'Seu desconto do inss é R${inss:.2f}')
    print(f'Seu desconto do fgts é R${inss:.2f}')
    print(f'O total de desconto é: R${inss + ir:.2f}')
    print(f'O seu sálario liquido é {salario - (inss + ir):.2f}')

elif 1500 < salario <= 2500:
    ir = (salario * 10) / 100
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    print(f'Seu sálario bruto é R${salario:.2f}')
    print(f'Seu desconto do ir é R${ir:.2f}')
    print(f'Seu desconto do inss é R${inss:.2f}')
    print(f'Seu desconto do fgts é R${inss:.2f}')
    print(f'O total de desconto é: R${inss + ir:.2f}')
    print(f'O seu sálario liquido é {salario - (inss + ir):.2f}')

else:
    ir = (salario * 20) / 100
    inss = (salario * 10) / 100
    fgts = (salario * 11) / 100
    print(f'Seu sálario bruto é R${salario:.2f}')
    print(f'Seu desconto do ir é R${ir:.2f}')
    print(f'Seu desconto do inss é R${inss:.2f}')
    print(f'Seu desconto do fgts é R${inss:.2f}')
    print(f'O total de desconto é: R${inss + ir:.2f}')
    print(f'O seu sálario liquido é {salario - (inss + ir):.2f}')
    