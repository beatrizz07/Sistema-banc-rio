from Cliente import Cliente
from Gerente import Gerente
#Importa as classes Cliente e Gerente de arquivos externos.

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
#Define a classe Conta, que representa uma conta bancária genérica.
#Inicializa a conta com um titular e um saldo inicial (padrão: R$ 0,00).
#Define os atributos titular e saldo.

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}"
        return "Valor inválido!"
#Método para realizar um depósito.
#Adiciona o valor ao saldo se for positivo.

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}"
        return "Saldo insuficiente ou valor inválido!"
#Método para realizar um saque.
#Reduz o saldo se o valor for válido e houver saldo suficiente.
    
    def mostrar_saldo(self):
        return f"Saldo: R$ {self.saldo:.2f}"
#Retorna o saldo da conta.

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=1000):
        super().__init__(titular, saldo)
        self.limite = limite
#Define a classe ContaCorrente, que herda de Conta.
#Inicializa a conta com um limite adicional de saque (padrão: R$ 1000,00).

    def sacar(self, valor):
        if valor > 0 and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}"
        return f"Saldo e limite insuficientes! Limite: R$ {self.limite:.2f}, Saldo: R$ {self.saldo:.2f}"
#Sobrescreve o método sacar da classe Conta.
#Permite saques dentro do limite disponível.

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, juros=0.05):
        super().__init__(titular, saldo)
        self.juros = juros
#Define a classe ContaPoupanca, que herda de Conta.
#Inicializa a conta com um atributo de taxa de juros (padrão: 5%).

    def aplicar_juros(self):
        self.saldo += self.saldo * self.juros
        return f"Juros aplicados! Novo saldo: R$ {self.saldo:.2f}"
#Aplica os juros ao saldo da conta.

def cadastrar_cliente():
    print("\n--- Cadastro do Cliente ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    email = input("Email: ")
    
    return Cliente(nome, cpf, telefone, endereco, email)
#Função que solicita os dados do cliente.
#Coleta os dados via input e cria um objeto Cliente.

def escolher_conta(cliente):
    print("\nEscolha o tipo de conta:")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")
    
    tipo_conta = input("Digite a opção (1 ou 2): ")
#Função que permite o cliente escolher entre ContaCorrente e ContaPoupanca.
#Exibe as opções e recebe a escolha do usuário.

    if tipo_conta == "1":
        conta = ContaCorrente(cliente)
        print("\nConta Corrente criada com sucesso!")
        return conta
    elif tipo_conta == "2":
        conta = ContaPoupanca(cliente)
        print("\nConta Poupança criada com sucesso!")
        return conta
    else:
        print("\nOpção inválida! Conta não criada.")
        return None
#Cria a conta escolhida ou exibe erro se a opção for inválida.

def main():
    gerente = Gerente("Carlos Almeida", "987.654.321-00", "99999-8888", "carlos@email.com", 7500.00)
    cliente = None  
    conta = None

    print("\n <3 Bem-vindo ao Banco <3")
#Função que gerencia o fluxo do programa.
#Cria um gerente e inicializa cliente e conta como None.
#Exibe a mensagem de boas-vindas.

    while True:
        print("\nOpções disponíveis:")
        print("1 - Cadastrar Cliente")
        print("2 - Ver dados do Cliente")
        print("3 - Ver dados do Gerente")
        print("4 - Depositar")
        print("5 - Sacar")
        print("6 - Ver saldo")
        print("7 - Aplicar juros (Conta Poupança)")
        print("8 - Sair")

        opcao = input("\nEscolha uma opção: ")
#Inicia um loop para o menu do sistema.
#Exibe o menu de opções.
#Lê a opção escolhida pelo usuário.

        if opcao == "1":
            cliente = cadastrar_cliente()
            conta = escolher_conta(cliente)
            if conta:
                print(f"Conta para {cliente.nome} criada com sucesso!")
#Cadastra um cliente e cria uma conta.

        elif opcao == "2":
            if cliente:
                print(cliente.mostrar_dados())
            else:
                print("\n❗ Nenhum cliente cadastrado. Cadastre um primeiro!")
#Exibe os dados do cliente, se existir.

        elif opcao == "3":
            print(gerente.mostrar_dados())
#Exibe os dados do gerente.

        elif opcao == "4":
            if conta:
                valor = float(input("Valor do depósito: R$ "))
                print(conta.depositar(valor))
            else:
                print("\n❗ Nenhum cliente cadastrado. Cadastre um primeiro!")
#Realiza um depósito, se houver uma conta cadastrada.

        elif opcao == "5":
            if conta:
                valor = float(input("Valor do saque: R$ "))
                print(conta.sacar(valor))
            else:
                print("\n❗ Nenhum cliente cadastrado. Cadastre um primeiro!")
#Realiza um saque, se houver uma conta cadastrada.

        elif opcao == "6":
            if conta:
                print(conta.mostrar_saldo())
            else:
                print("\n❗ Nenhum cliente cadastrado. Cadastre um primeiro!")
#Exibe o saldo da conta.

        elif opcao == "7":
            if isinstance(conta, ContaPoupanca):
                print(conta.aplicar_juros())
            else:
                print("\n❗ Somente contas poupança podem aplicar juros.")
#Aplica juros se a conta for ContaPoupanca.

        elif opcao == "8":
            print("\nSaindo... Obrigado por usar nosso sistema bancário!")
            break
#Sai do programa.

        else:
            print("\n❌ Opção inválida! Tente novamente.")
#Exibe erro para opções inválidas.

if __name__ == "__main__":
    main()
#Executa main() se o script for executado diretamente.

