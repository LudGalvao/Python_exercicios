import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros = area / 6 * 1.1 
latas = math.ceil(litros / 18) 
galoes = math.ceil(litros/ 3.6) 


preco_latas = latas * 80
print(f"Para pintar {area:.2f} m² você precisará de {latas} lata(s) de 18 litros de tinta, ao preço de R${preco_latas:.2f}.")

# comprando apenas galões de 3,6 litros
preco_galoes = galoes * 25
print(f"Para pintar {area:.2f} m² você precisará de {galoes} galão(ões) de 3,6 litros de tinta, ao preço de R${preco_galoes:.2f}.")

# misturando latas e galões
latas_necessarias = int(litros / 18) # parte inteira da divisão
resto = litros % 18 # o que sobrou da divisão
galoes_necessarios = math.ceil(resto / 3.6) # arredondando para cima
preco_misto = latas_necessarias * 80 + galoes_necessarios * 25
print(f"Para pintar {area:.2f} m² você precisará de {latas_necessarias} lata(s) de 18 litros e {galoes_necessarios} galão(ões) de 3,6 litros de tinta, ao preço de R${preco_misto:.2f}.")
