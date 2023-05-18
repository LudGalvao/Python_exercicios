class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f'Depósito: +{valor}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(f'Saque: -{valor}')
        else:
            print('Saldo insuficiente.')

    def imprimir_extrato(self):
        print(f"Saldo atual: {self.saldo}")
        print("Histórico de transações:")
        for transacao in self.transacoes:
            print(transacao)


titular = input("Informe o nome do titular: ")
saldo = float(input("Informe seu saldo atual: "))
conta = Conta(titular, saldo)

depositar = input("Deseja fazer um depósito (s/n): ")

if depositar.lower() == "s":
    deposito = float(input("Informe o valor para depositar: "))
    conta.depositar(deposito)
    print(f"Seu saldo atual é de R${conta.saldo:.2f}")

sacar = input("Deseja realizar um saque (s/n): ")

if sacar.lower() == "s":
    saque = float(input("Informe o valor para fazer o saque: "))
    conta.sacar(saque)
    print(f"Seu saldo atual é de R${conta.saldo:.2f}")

extrato = input("Deseja ver o seu extrato (s/n): ")

if extrato.lower() == "s":
    conta.imprimir_extrato()

    
