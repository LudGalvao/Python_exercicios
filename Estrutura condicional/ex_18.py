dia = int(input("Informe um dia no formato dd: "))
mes = int(input("Informe um mês no formato mm: "))
ano = int(input("Informe um ano no formato aaaa: "))

if dia > 31 or mes > 12 or ano < 0:
    print("Inválido")

else:
    print(f"{dia}/{mes}/{ano}")
