import random


class Gerador_CPF:
    def __init__(self):
        self.base_cpf = [random.randint(0, 9) for _ in range(9)]

    def gerar(self):
        cpf = self.base_cpf[:]
        cpf.append(self._calcular_digito(cpf))
        cpf.append(self._calcular_digito(cpf))
        return self._formatar_cpf(cpf)

    def _calcular_digito(self, cpf):
        peso = len(cpf) + 1
        total = sum([digito * peso for digito, peso in zip(cpf, range(peso, 1, -1))])
        resto = total % 11
        return (11 - resto) if resto > 1 else 0

    def _formatar_cpf(self, cpf):
        cpf_str = ''.join(map(str, cpf))
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"


gerador = Gerador_CPF()
cpf = gerador.gerar()
print(cpf)
