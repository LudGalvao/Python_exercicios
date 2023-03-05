download = float(input('informe o tamanho do arquivo em mb: '))
velocidade = int(input('Informe a velocidade em mbps da sua internet: '))
calc = download / (velocidade / 8)
tempo = calc / 60

print(f'Para fazer o download de um aquivo {int(download)}mbs com velocidade de {velocidade}mbps, você vai levar {tempo:.1f}min')