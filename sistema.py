class Conta:
    def __init__(self, titular, saldo=0, limite=5000):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor):
        self.saldo += valor
        return f"{self.titular.nome} depositou R$ {valor}. Saldo atual: R$ {self.saldo}"
    
    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            return "Saldo insuficiente, incluindo limite!"
        else:
            self.saldo -= valor
            return f"{self.titular.nome} sacou R$ {valor}. Saldo atual: R$ {self.saldo}"
    
    def mostrar_saldo(self):
        return f"Saldo de {self.titular.nome}: R$ {self.saldo}, Limite disponível: R$ {self.limite}"


class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=5000):
        super().__init__(titular, saldo, limite)


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, limite=5000, taxa_rendimento=0.005):
        super().__init__(titular, saldo, limite)
        self.taxa_rendimento = taxa_rendimento
    
    def aplicar_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.saldo += rendimento
        return f"Rendimento aplicado! Novo saldo: R$ {self.saldo:.2f}"
    
from Cliente import Cliente
from Gerente import Gerente

def main():
    cliente = Cliente("Mariana Castro", "123.456.789-00", "(88) 99999-9999", "Cedro-ce")
    conta_corrente = ContaCorrente(cliente, saldo=1000, limite=5000)
    conta_poupanca = ContaPoupanca(cliente, saldo=5000, limite=500)
    gerente = Gerente("Carlos Souza", "GR12345", "Atendimento")
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver dados do cliente")
        print("2 - Depositar na Conta Corrente")
        print("3 - Sacar da Conta Corrente")
        print("4 - Ver saldo da Conta Corrente")
        print("5 - Aplicar rendimento na Conta Poupança")
        print("6 - Ver saldo da Conta Poupança")
        print("7 - Ver dados do gerente")
        print("8 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            print(cliente.mostrar_dados())
        elif opcao == "2":
            valor = float(input("Valor para depósito: "))
            print(conta_corrente.depositar(valor))
        elif opcao == "3":
            valor = float(input("Valor para saque: "))
            print(conta_corrente.sacar(valor))
        elif opcao == "4":
            print(conta_corrente.mostrar_saldo())
        elif opcao == "5":
            print(conta_poupanca.aplicar_rendimento())
        elif opcao == "6":
            print(conta_poupanca.mostrar_saldo())
        elif opcao == "7":
            print(gerente.mostrar_dados())
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
