class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self):
        self.salario *= 1.10  

nome = input("Informe seu nome: ")
cargo = input("Informe seu cargo: ")
salario = float(input("Informe seu salário: "))

funcionario = Funcionario(nome, cargo, salario)
funcionario.aumentar_salario()

aumento_salarial = funcionario.salario

print(f"Seu nome é {nome}")
print(f"Seu cargo atual é {cargo}")
print(f"O seu salário antigo era R${salario:.2f}, com o aumento de 10% ficou R${aumento_salarial:.2f}")
