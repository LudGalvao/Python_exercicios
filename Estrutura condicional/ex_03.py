print('f para "Feminino" ou m para "Masculino"')
sexo = str(input('Digite uma letra: '))

if sexo == 'f' or sexo == 'F':
    print('Seu sexo é feminino')
elif sexo == 'm' or sexo == 'M':
    print('Seu sexo é masculino')
else:
    print('Invalido')