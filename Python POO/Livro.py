class Livro:
    def __init__(self, titulo, editora, autor, qtd_paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.paginas = qtd_paginas

    def longo(self):
        if self.paginas >= 500:
            return "É considerado um livro longo."
        elif self.paginas <= 350:
            return "É considerado um livro médio"
        else:
            return "É considerado um livro curto"
        
    def informacoes(self):
        return print(f"O nome do livro é {self.titulo},\nO autor do livro é {self.autor},\nO livro tem {self.paginas} páginas e {self.longo()}")
    

titulo = input("Informe o nome do livro: ")
autor = str(input("Informe o nome do autor: "))
editora = str(input("Informe o nome da editora: "))
qtd_paginas = int(input("Informe a quantidade de páginas do livro: "))
livro = Livro(titulo, autor, editora, qtd_paginas)

livro.informacoes()
