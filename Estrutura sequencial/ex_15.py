ganha_hora = float(input("Informe quanto você ganha por hora: "))
mensal_hora = int(input("Informe quantas horas você trabalha por mês: "))

salario_bruto = (ganha_hora * mensal_hora) 
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sind = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - ir - inss - sind

print(f'Seu sálario bruto é R$ {salario_bruto:.2f}')
print(f'Você precisa pagar ao imposto de renda R$ {ir:.2f}')
print(f'Você precisa pagar ao Inss R$ {inss:.2f}')
print(f'Você precisa pagar ao sindicato R$ {sind:.2f}')
print(f'Seu sálario liquido é R$ {salario_liquido:.2f}')