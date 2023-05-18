class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def ano_canino(self):
        return self.idade * 7
    
nome = str(input("Informe o nome do cachorro: "))
idade = int(input("Informe a idade canina do cachorro: "))
raca = str(input("Informe a raça do cachorro: "))

cachorro = Cachorro(nome,idade,raca)

print()
print(f"O {nome} é da raça {raca}.\n Ele possui {idade} anos canino e {cachorro.ano_canino()} de anos humano.")

