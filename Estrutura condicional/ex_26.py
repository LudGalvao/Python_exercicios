escolha = str(input("(A - Alcool / G - Gasolina): "))

if escolha == "A" or escolha == "a":
    alcool = float(input("Informe quantos litros você deseja: "))
    
    if alcool <= 20:
        total = alcool * 1.90
        desconto = total * (3 / 100)
        valor = total - desconto
        print(f"Você pediu {int(alcool)}l de alcool e teve um desconto de 3% a cada litro. O valor total é R${valor:.2f}")

    else:
        total = alcool * 1.90
        desconto = total * (5 / 100)
        valor = total - desconto
        print(f"Você pediu {int(alcool)} litros de alcool e teve um desconto de 3% a cada litro. O valor total é R${valor:.2f}")

elif escolha == "G" or escolha == "g":
    gasolina = float(input("Informe quantos litros você deseja: "))

    if gasolina <= 20:
        total = gasolina * 2.50
        desconto = total * (4 / 100)
        valor = total - desconto
        print(f"Você pediu {int(gasolina)} litros de gasolina e teve um desconto de 3% a cada litro. O valor total é R${valor:.2f}")

    else:
        total = gasolina * 2.50
        desconto = total * (6 / 100)
        valor = total - desconto
        print(f"Você pediu {int(gasolina)} litros de gasolina e teve um desconto de 3% a cada litro. O valor total é R${valor:.2f}")

else:
    print("Escolha inválida")