class Cliente:
    def __init__(self, codigo, endereco):
        self.codigo = codigo
        self.endereco = endereco
    # def __str__(self):
        # return " Codigo: {} \n Endereco: {}" .format(self.codigo, self.endereco)

    def localizar_endereco(self):
        pass

class Cliente_Fisico(CLIENTE):
    def __init__(self, nome, cpf, codigo, endereco):
        super().__init__(codigo, endereco)
        self.nome = nome
        self.cpf = cpf
    # def __str__(self):
        # return super().__str__() + '\n Nome: {} \n CPF: {}' .format(self.nome, self.cpf)

    def verificar_cpf(self):
        pass

class Cliente_Juridico(CLIENTE):
    def __init__(self, codigo, endereco, cnpj, razao_social):
        super().__init__(codigo, endereco)
        self.cnpf = cnpj
        self.razao_social = razao_social
    # def __str__(self):
        # return super().__str__() + '\n CNPJ: {} \n Razão Social: {}' .format(self.cnpf, self.razao_social)

    def verificar_cnpj(self):
        pass