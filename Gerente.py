class Gerente:
    def __init__(self, nome, cpf, telefone, email, salario):
        self.nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__salario = salario
    
    def mostrar_dados(self):
        return f"\nGerente:\nNome: {self.nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nEmail: {self.__email}\nSalário: R$ {self.__salario:.2f}\n"

#Define uma classe chamada Gerente.
#Define o método construtor __init__, que inicializa os atributos do objeto.
#Atributo público nome, acessível diretamente.
#Atributos privados (__cpf, __telefone, __email, __salario), acessíveis apenas dentro da classe.
#Atributos privados (__cpf, __telefone, __email, __salario), acessíveis apenas dentro da classe.
#Retorna uma string formatada com os dados do gerente, incluindo o salário com duas casas decimais.
