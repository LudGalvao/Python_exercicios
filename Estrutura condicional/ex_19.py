numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número inválido! Digite um número menor que 1000.")
else:
    centenas, dezenas, unidades = [int(digito) for digito in str(numero).zfill(3)] # o zfill garante sempre que vai ter 3 digitos.

    resultado = ", ".join([f"{digito} {unidade}" for digito, unidade in zip([centenas, dezenas, unidades], ["centenas", "dezenas", "unidades"]) if digito> 0])

    print(resultado)
