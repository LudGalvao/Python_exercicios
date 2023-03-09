print("Responda as perguntas abaixo sobre o crime:")
resposta1 = input("Telefonou para a vítima? (Sim ou Não) ")
resposta2 = input("Esteve no local do crime? (Sim ou Não) ")
resposta3 = input("Mora perto da vítima? (Sim ou Não) ")
resposta4 = input("Devia para a vítima? (Sim ou Não) ")
resposta5 = input("Já trabalhou com a vítima? (Sim ou Não) ")

respostas_positivas = 0
if resposta1.lower() == "sim":
    respostas_positivas += 1
if resposta2.lower() == "sim":
    respostas_positivas += 1
if resposta3.lower() == "sim":
    respostas_positivas += 1
if resposta4.lower() == "sim":
    respostas_positivas += 1
if resposta5.lower() == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é Suspeito(a) do crime.")
elif respostas_positivas >= 3 and respostas_positivas <= 4:
    print("Você é Cúmplice do crime.")
elif respostas_positivas == 5:
    print("Você é o Assassino do crime.")
else:
    print("Você é Inocente do crime.")
