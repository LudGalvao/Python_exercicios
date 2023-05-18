class Tarefas:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluido = False

    def marcar_como_concluida(self):
        self.concluido = True

    def mostrar_tarefa(self):
        return self.titulo
    
    def esta_concluida(self):
        if self.concluido:
            return f"A Tarefa {self.titulo} foi concluída"
        else:
            return f"A Tarefa {self.titulo} está pendente"

tarefas = []

while True:
    titulo = input("Informe a Tarefa (0 para encerrar o programa): ")

    if titulo == "0":
        break

    tarefas.append(Tarefas(titulo))

mostrar_tarefas = input("Deseja visualizar as suas Tarefas (s/n): ")

if mostrar_tarefas.lower() == "s":
    for tarefa in tarefas:
        print(tarefa.mostrar_tarefa())

status_tarefa = input("Deseja informar o status da tarefa (x = concluir / n = pendente) (s/n): ")

if status_tarefa.lower() == "s":
    for tarefa in tarefas:
        opcao = input(f"Informe o status da tarefa '{tarefa.mostrar_tarefa()}': ")
        if opcao.lower() == "x":
            tarefa.marcar_como_concluida()

for tarefa in tarefas:
    print(tarefa.esta_concluida())
