peso = float(input("Informe o peso: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"O excesso foi de {excesso:.1f}kg e o valor da multa é R${multa:.2f}")

else:
    print("Você não passou o peso de 50kg")