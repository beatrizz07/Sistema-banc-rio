from Cliente import Cliente
from Gerente import Gerente
import time
#Importa as classes Cliente e Gerente de arquivos externos.
#Importa a biblioteca time 

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, valor):
        pass
#Define a classe Conta, que representa uma conta bancária genérica.
#Inicializa a conta com um titular e um saldo inicial (padrão: R$ 0,00).
#Define os atributos titular e saldo.
#Define o método sacar que recebe o valor a ser sacado, mas ainda não tem implementação
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"✅ Depósito de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}"
        return "⚠️ Valor inválido!"
#Método para realizar um depósito.
#Adiciona o valor ao saldo se for positivo.

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"✅ Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}"
        return "🚫 Saldo insuficiente ou valor inválido!"
#Método para realizar um saque.
#Reduz o saldo se o valor for válido e houver saldo suficiente.

    def mostrar_saldo(self):
        return f"💰 Saldo disponível: R$ {self.saldo:.2f}"
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
            return f"✅ Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}"
        return f"🚫 Saldo e limite insuficientes! Limite: R$ {self.limite:.2f}, Saldo: R$ {self.saldo:.2f}"
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
        return f"📈 Juros aplicados! Novo saldo: R$ {self.saldo:.2f}"
#Aplica os juros ao saldo da conta.

def cadastrar_cliente():
    print("\n📋 Cadastro do Cliente")
    nome = input("👤 Nome: ")
    cpf = input("🆔 CPF: ")
    telefone = input("📞 Telefone: ")
    endereco = input("🏠 Endereço: ")
    email = input("📧 Email: ")
    return Cliente(nome, cpf, telefone, endereco, email)
#Função que solicita os dados do cliente.
#Coleta os dados via input e cria um objeto Cliente.

def escolher_conta(cliente):
    print("\n💳 Escolha o tipo de conta:")
    print("1️⃣ Conta Corrente")
    print("2️⃣ Conta Poupança")
    tipo_conta = input("Digite a opção (1 ou 2): ")
#Função que permite o cliente escolher entre ContaCorrente e ContaPoupanca.
#Exibe as opções e recebe a escolha do usuário.
    
    if tipo_conta == "1":
        return ContaCorrente(cliente)
    elif tipo_conta == "2":
        return ContaPoupanca(cliente)
    else:
        print("❌ Opção inválida!")
        return None
#Cria a conta escolhida ou exibe erro se a opção for inválida.

def login_cliente(clientes):
    cpf = input("🆔 Digite seu CPF: ")
    for cliente, conta in clientes:
        if cliente.get_cpf() == cpf:
            print(f"✅ Login bem-sucedido! Bem-vindo, {cliente.nome}!")
            return cliente, conta
    print("❌ CPF não encontrado! Cadastre-se primeiro.")
    return None, None
#Solicita ao usuário que digite o CPF.
#Percorre uma lista de clientes e contas.
#Verifica se o CPF informado corresponde ao de um cliente.
#Exibe uma mensagem de sucesso com o nome do cliente.
#Retorna o cliente e a conta se o login for bem sucedido.
#Exibe uma mensagem de erro se o CPF não for encontrado.
#Retorna None caso o CPF não seja encontrado

def main():
    gerente = Gerente("Carlos Almeida", "987.654.321-00", "99999-8888", "carlos@email.com", 7500.00)
    
    clientes = []
#Função que gerencia o fluxo do programa. 
#Cria um objeto gerente da classe Gerente com os dados fornecidos.
#Cria uma lista vazia chamada clientes para armazenar os clientes cadastrados.

    print("\n💙 Bem-vindo ao Banco Digital 💙")
    while True:
        print("\n🔹 Menu 🔹")
        print("1️⃣ Cadastrar Cliente")
        print("2️⃣ Login Cliente")
        print("3️⃣ Ver dados do Gerente")
        print("4️⃣ Sair")

        opcao = input("\nEscolha uma opção: ")
#Exibe a mensagem de boas-vindas.
#Inicia um loop infinito que continuará até que seja quebrado explicitamente.
#Exibe o título "Menu" com um ícone de menu.
#Exibe a opção 1 para cadastrar um cliente.
#Exibe a opção 2 para login do cliente.
#Exibe a opção 3 para ver os dados do cliente.
#Exibe a opção 4 para sair
#Solicita ao usuário que escolha uma opção e armazene a resposta na variável opcao.
        
        if opcao == "1":
            cliente = cadastrar_cliente()
            conta = escolher_conta(cliente)
            if conta:
                clientes.append((cliente, conta))
                print(f"✅ Conta para {cliente.nome} criada com sucesso!")
        
        elif opcao == "2":
            cliente, conta = login_cliente(clientes)
            if cliente:
                while True:
                    print("\n🔹 Opções da Conta 🔹")
                    print("1️⃣ Ver dados do Cliente")
                    print("2️⃣ Depositar")
                    print("3️⃣ Sacar")
                    print("4️⃣ Ver saldo")
                    print("5️⃣ Aplicar juros (Conta Poupança)")
                    print("6️⃣ Sair")
                    opcao_conta = input("Escolha uma opção: ")
#Essa parte do código verifica a opção escolhida pelo usuário. 
#Se for "1", chama as funções para cadastrar um cliente e escolher o tipo de conta. 
#Se a conta for criada, ela é adicionada à lista de clientes. 
#Se a opção for "2", chama a função para realizar o login do cliente. 
#Após o login bem-sucedido, exibe um menu com opções para o cliente.
                    
                    if opcao_conta == "1":
                        print(cliente.mostrar_dados())
                    elif opcao_conta == "2":
                        valor = float(input("💰 Valor do depósito: R$ "))
                        print(conta.depositar(valor))
                    elif opcao_conta == "3":
                        valor = float(input("🏧 Valor do saque: R$ "))
                        print(conta.sacar(valor))
                    elif opcao_conta == "4":
                        print(conta.mostrar_saldo())
                    elif opcao_conta == "5" and isinstance(conta, ContaPoupanca):
                        print(conta.aplicar_juros())
                    elif opcao_conta == "6":
                        break
                    else:
                        print("❌ Opção inválida! Tente novamente.")
        
        elif opcao == "3":
            print(gerente.mostrar_dados())
        elif opcao == "4":
            print("👋 Saindo... Obrigado por usar nosso banco!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
#Essa parte do código lida com as opções do menu da conta do cliente. 
#Dependendo da escolha, ele executa ações como mostrar os dados do cliente, fazer depósitos, 
#saques, verificar saldo, aplicar juros (se for uma conta de poupança), ou sair do menu de opções. 
#Se houver opção para inválida, exibe uma mensagem de erro. 
#Quando a opção "6" é escolhida, o loop é interrompido. 
#Se a opção escolhida para "3", exibe os dados do gerente. 
#Se houver opção para "4", sai do programa.
        
        time.sleep(1)
#Faz o programa pausar por 1 segundo antes de continuar a execução. 

if __name__ == "__main__":
    main()
#Executa main() se o script for executado diretamente.