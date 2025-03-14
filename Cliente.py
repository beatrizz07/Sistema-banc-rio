class Cliente:
    def __init__(self, nome, cpf, telefone, endereco, email):
        self.nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__email = email
    
    def mostrar_dados(self):
        return f"\nCliente:\nNome: {self.nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nEndereço: {self.__endereco}\nEmail: {self.__email}\n"