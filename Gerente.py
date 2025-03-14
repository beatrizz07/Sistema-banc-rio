class Gerente:
    def __init__(self, nome, cpf, telefone, email, salario):
        self.nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__salario = salario
    
    def mostrar_dados(self):
        return f"\nGerente:\nNome: {self.nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nEmail: {self.__email}\nSalário: R$ {self.__salario:.2f}\n"
