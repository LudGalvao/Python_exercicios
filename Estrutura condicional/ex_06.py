num_1 = int(input('Informe o primeiro número: '))
num_2 = int(input('Informe o segundo número: '))
num_3 = int(input('Informe o terceiro número: '))

if num_1 > num_2 and num_1 > num_3:
    print('O primeiro número é maior')
elif num_2 > num_1 and num_2 > num_3:
    print('O segundo número é maior')
else:
    print('O terceiro número é maior')
    