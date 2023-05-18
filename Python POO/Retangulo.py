class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)
    
altura = float(input("Informe a altura do Retangulo: "))
largura = float(input("Informe a largura do Retangulo: "))
retangulo = Retangulo(altura, largura)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print(f"A area do Retangulo é {area}")
print(f"O perimetro do Retangulo é {perimetro}")
