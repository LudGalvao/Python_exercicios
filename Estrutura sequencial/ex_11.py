numero_1 = int(input("Informe um número: "))
numero_2 = int(input("Informe outro número: "))
numero_3 = float(input("Informe outro número: "))

calc_1 = (numero_1 * 2) + (numero_2 - (numero_2 / 2))
calc_2 = (numero_1 * 3) + numero_3
calc_3 = numero_3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {calc_1:.0f}")
print(f"A soma do triplo do primeiro com o terceiro: {calc_2:.0f}")
print(f"O terceiro elevado ao cubo: {calc_3:.0f}")