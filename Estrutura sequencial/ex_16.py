import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros = area / 3
latas = math.ceil(litros / 18)
preco_total = latas * 80

print(f"Para pintar {area:.2f} m² você precisará de {latas} lata(s) de 18 litros de tinta, ao preço total de R${preco_total:.2f}.")
