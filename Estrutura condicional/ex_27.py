morango_5kg = 2.50
morango_acima_5kg = 2.20
maca_5kg = 1.80
maca_acima_5kg = 1.50

quantidade_morango = float(input("Digite a quantidade (em Kg) de morangos comprados: "))
quantidade_maca = float(input("Digite a quantidade (em Kg) de maçãs comprados: "))


if quantidade_morango <= 5:
    preco_total_morango = quantidade_morango * morango_5kg
else:
    preco_total_morango = quantidade_morango * morango_acima_5kg

if quantidade_maca <= 5:
    preco_total_maca = quantidade_maca * maca_5kg
else:
    preco_total_maca = quantidade_maca * maca_acima_5kg

preco_total_frutas = preco_total_morango + preco_total_maca

if preco_total_frutas > 25 or quantidade_morango + quantidade_maca > 8:
    desconto = 0.1 * preco_total_frutas
else:
    desconto = 0

preco_final = preco_total_frutas - desconto

print(f"O valor a ser pago é de R$ {preco_final:.2f}.")
