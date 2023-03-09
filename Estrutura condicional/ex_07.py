num_1 = int(input('Informe o primeiro número: '))
num_2 = int(input('Informe o segundo número: '))
num_3 = int(input('Informe o terceiro número: '))

if num_1 < num_2 and num_1 < num_3:
    print(f'O número {num_1} é o menor número')
    if num_2 > num_1 and num_2 > num_3:
        print(f'O número {num_2} é o maior número')
    elif num_3 > num_1 and num_3 > num_2:
        print(f'O numero {num_3} é maior número')

elif num_2 < num_1 and num_2 < num_3:
    print(f'O número {num_2} é o menor número')
    if num_1 > num_2 and num_1 > num_3:
        print(f'O número {num_1} é o maior número')
    elif num_3 > num_1 and num_3 > num_2:
        print(f'O numero {num_3} é maior número')

else:
    print(f'O número {num_3} é o menor número')
    if num_1 > num_2 and num_1 > num_3:
         print(f'O número {num_1} é o maior número')
    elif num_2 > num_1 and num_2 > num_3:
          print(f'O número {num_2} é o maior número')

