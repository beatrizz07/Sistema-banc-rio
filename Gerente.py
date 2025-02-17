class Gerente:
    def __init__(self, nome, cnpj, setor):
        self.nome = nome
        self.cnpj = cnpj
        self.setor = setor
    
    def mostrar_dados(self):
        return f"Gerente: {self.nome}, CNPJ: {self.cnpj}, Setor: {self.setor}"
