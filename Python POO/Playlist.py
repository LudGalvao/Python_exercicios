class Playlist:
    def __init__(self, artista, album):
        self.artista = artista
        self.album = album
        self.musica = []

    def add_musica(self, musica):
         self.musica.append(musica)
    
    def remover_musica(self):
        if self.musica:
            return self.musica.pop()
        else:
            return None
    
    def informacoes(self):
        print(f"Artista: {self.artista}\n Album: {self.album}\n Musicas: {self.musica}")

artista = input("Informe o nome do artista: ")
album = input("Informe o nome do album: ")

playlist = Playlist(artista, album)

while True:
    musicas = input("Informe o nome da musica(0 para encerrar): ")

    if musicas == "0":
        break

    playlist.add_musica(musicas)

playlist.informacoes()
