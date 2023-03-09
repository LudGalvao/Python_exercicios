print('M = MATUTINO, V = VESPERTINO, N = NOTURNO')
turno = str(input('Informe o seu turno: '))

if turno == 'M' or turno == 'm':
    print('Bom dia')
elif turno == 'V' or turno == 'v':
    print('Boa tarde')
elif turno == 'N' or turno == 'n':
    print('Boa noite')
else:
    print('Opção invalida')