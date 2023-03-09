print("1 - File Duplo \tAté 5 Kg: R$ 4,90 por Kg \tAcima de 5 Kg: R$ 5,80 por Kg")
print("2 - Alcatra \tAté 5 Kg: R$ 5,90 por Kg \tAcima de 5 Kg: R$ 6,80 por Kg")
print("3 - Picanha \tAté 5 Kg: R$ 6,90 por Kg \tAcima de 5 Kg: R$ 7,80 por Kg")

opcao = int(input("Digite o número correspondente ao tipo de carne desejado: "))
quantidade = float(input("Digite a quantidade desejada (em Kg): "))

if opcao == 1:
    if quantidade <= 5:
        preco_total = quantidade * 4.9
    else:
        preco_total = quantidade * 5.8
elif opcao == 2:
    if quantidade <= 5:
        preco_total = quantidade * 5.9
    else:
        preco_total = quantidade * 6.8
elif opcao == 3:
    if quantidade <= 5:
        preco_total = quantidade * 6.9
    else:
        preco_total = quantidade * 7.8
else:
    print("Opção inválida. Por favor, digite o número correspondente a uma das opções de carne da promoção.")

print("---- CUPOM FISCAL ----")
if opcao == 1:
    tipo_carne = "File Duplo"
    preco_ate_5 = 4.9
    preco_acima_5 = 5.8
elif opcao == 2:
    tipo_carne = "Alcatra"
    preco_ate_5 = 5.9
    preco_acima_5 = 6.8
elif opcao == 3:
    tipo_carne = "Picanha"
    preco_ate_5 = 6.9
    preco_acima_5 = 7.8
else:
    tipo_carne = "Opção inválida"

print("Tipo de carne: ", tipo_carne)
print("Quantidade: ", quantidade, " Kg")
print("Preço total: R$ {:.2f}".format(preco_total))

tipo_pagamento = input("Digite o tipo de pagamento (Cartão / Outro): ")
if tipo_pagamento == "Cartão":
    desconto = preco_total * 0.05
else:
    desconto = 0.0

valor_a_pagar = preco_total - desconto
print("Tipo de pagamento: ", tipo_pagamento)
print("Valor do desconto: R$ {:.2f}".format(desconto))
print("Valor a pagar: R$ {:.2f}".format(valor_a_pagar))
