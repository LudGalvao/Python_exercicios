valor_saque = int(input("Qual o valor do saque? (Mínimo: R$10; Máximo: R$600) "))
notas = [100, 50, 10, 5, 1]
contador_notas = [0, 0, 0, 0, 0] # lista para contar as notas a serem fornecidas

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido.")
else:
    contador_notas[0] = valor_saque // notas[0]
    valor_saque %= notas[0]

    contador_notas[1] = valor_saque // notas[1]
    valor_saque %= notas[1]

    contador_notas[2] = valor_saque // notas[2]
    valor_saque %= notas[2]

    contador_notas[3] = valor_saque // notas[3]
    valor_saque %= notas[3]

    contador_notas[4] = valor_saque // notas[4]

    print("Notas fornecidas:")
    for i, nota in enumerate(notas):
        if contador_notas[i] > 0:
            print("{} nota(s) de R${}".format(contador_notas[i], nota))
