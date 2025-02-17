class Cliente:
    def __init__(self, nome, cpf, telefone, endereço):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereço = endereço
    
    def mostrar_dados(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereço}"