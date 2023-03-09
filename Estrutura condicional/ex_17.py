ano = int(input("Informe o ano: "))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto')
elif ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
elif ano % 100 == 0:
    print(f'O ano {ano} não é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
