class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def media(self):
        return sum(self.notas) / 4

    def aprovado(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

    def verificar_dados_aluno(self, nome, notas):
        if any(char.isdigit() for char in nome):
            raise ValueError("O nome do aluno não pode conter números.")

        for nota in notas:
            if nota < 0 or nota > 10:
                raise ValueError("As notas devem estar no intervalo de 0 a 10.")


alunos = []

while True:
    nome = input("Informe o nome do aluno (ou 0 para encerrar): ")

    if nome == "0":
        break

    idade = int(input("Informe a idade do aluno: "))
    notas = []

    for i in range(4):
        nota_individual = float(input("Informe a nota do aluno: "))
        notas.append(nota_individual)

    aluno = Aluno(nome, idade, notas)
    aluno.verificar_dados_aluno(nome, notas)
    situacao = aluno.aprovado()

    alunos.append({
        "Nome": aluno.nome,
        "Notas": aluno.notas,
        "Situação": situacao
    })

for aluno in alunos:
    print("Nome:", aluno["Nome"])
    print("Notas:", aluno["Notas"])
    print("Situação:", aluno["Situação"])
    print()
