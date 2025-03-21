
class Cliente:
    def __init__(self, nome, cpf, telefone, endereco, email):
        self.nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__email = email
        
    def mostrar_dados(self):
        return f"\nCliente:\nNome: {self.nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nEndereço: {self.__endereco}\nEmail: {self.__email}\n"

#Define uma classe chamada Cliente.
#Define o método construtor __init__, que inicializa os atributos do objeto.
#Atributo público nome, acessível diretamente.
#Atributos privados (__cpf, __telefone, __endereco, __email), acessíveis apenas dentro da classe.
#Define o método mostrar_dados, responsável por exibir as informações do cliente.
#Retorna uma string formatada com os dados do cliente, incluindo os atributos privados.
