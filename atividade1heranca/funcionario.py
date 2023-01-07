class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    # def __str__(self):
        # return " Nome: {} \n CPF: {} \n Salário: {}" .format(self.nome, self.cpf, self.salario)

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, qualdepartamento, gratificacao):
        super().__init__(nome, cpf, salario)
        self.qualdepartamento = qualdepartamento
        self.gratificacao = gratificacao
    # def __str__(self):
        # return super().__str__() + "\n Departamento: {} \n Gratificação: {}" .format(self.qualdepartamento, self.gratificacao)

class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario, qualescritorio):
        super().__init__(nome, cpf, salario)
        self.qualescritorio = qualescritorio
    # def __str__(self):
        # return super().__str__() + "\n Escritorio: {}" .format(self.qualescritorio)