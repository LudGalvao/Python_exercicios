import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
raio = float(input("Informe o raio do circulo: "))
circulo = Circulo(raio)

area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()

print(f"A area do Circulo é {area:.2f}")
print(f"O perimetro do Circulo é {perimetro:.2f}")
