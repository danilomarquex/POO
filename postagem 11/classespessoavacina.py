import datetime
data_atual = datetime.datetime.now()
ano_atual = data_atual.year

class vacina_covid19:

    def __init__(self, numero_registro, local, tipo, datadose1, datadose2 = None):
        self.__numero_registro = numero_registro
        self.__local  = local #estado
        self.__tipo = tipo
        self.__datadose1 = datadose1
        self.__datadose2 = datadose2

    def __str__(self):
        return "numero_registro da vacina: {}" + ' ' + "local: {}" +' '+ "tipo: {}" +' '+ "Data da primeira dose: {}" +' '+ "Data da Aplicação da segunda dose: {}" .format(self.__numero_registro, self.__local, self.__tipo, self.__datadose1, self.__datadose2)

    @property
    def numero_registro(self):
        return self.__numero_registro

    @numero_registro.setter
    def numero_registro(self, valor):
        print('sem permissão!')

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, valor):
        print('sem permissão!!!')

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        print('sem permissão!!!')

    @property
    def datadose1(self):
        return self.__datadose1

    @datadose1.setter
    def datadose1(self, valor):
        print('sem permissão!!!!')

    @property
    def datadose2(self):
        return self.__datadose2

    @datadose2.setter
    def datadose2(self, valor):
        self.__datadose2 = valor

class Pessoa:
    
    def __init__(self, cpf, nome, data_nascimento, possui_comorbidade = 'NÂO', descricao_comorbidade = None, vacina_covid = None):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__possui_comorbidade = possui_comorbidade
        self.__descricao_comorbidade = descricao_comorbidade
        self.__vacina_covid = vacina_covid
    
    def __str__(self):
        return " CPF: {} \n Nome: {} \n Data de Nascimento: {} \n Cormobidades: {} \n Descrição de comorbidades: {} \n Vacina Covid: {}".format(self.__cpf, self.__nome, self.__data_nascimento, self.__possui_comorbidade, self.__descricao_comorbidade, self.__vacina_covid)

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        print('sem permissão!!')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        print('sem permissão!!')

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        print('sem permissão!!')

    @property
    def possui_comorbidade(self):
        if self.__possui_comorbidade.upper() == 'SIM':
            return self.__descricao_comorbidade
        else:
            return "Não possui comorbidades!!!"
    
    @possui_comorbidade.setter
    def possui_comorbidade(self, valor):
        print('sem permissão!!!')

    @property
    def descricao_comorbidade(self):
        return self.__descricao_comorbidade

    @descricao_comorbidade.setter
    def descricao_comorbidade(self, valor):
        print('sem permissão!!')

    @property
    def vacina_covid(self):
        if self.__vacina_covid != None:
            return self.__vacina_covid.tipo
        else:
            return "Sem vacina!"

    @vacina_covid.setter
    def vacina_covid(self, valor):
        print('sem permissão!!')

    def getIdade(self):
        idade = (ano_atual - (self.data_nascimento))
        print("Idade: {}" .format(idade))

    def vacinardose1(self, numero_registro, local, tipo, datadose1 = datetime.datetime.today(), datadose2 = None):
        if (ano_atual-(self.__data_nascimento)) > 60 or (ano_atual-(self.__data_nascimento)) > 18 and self.__possui_comorbidade.upper() == 'SIM':
            if vacina_covid19 == None:
                v1=vacina_covid19(numero_registro, local, tipo, datadose1, datadose2)
                if type(v1) == vacina_covid19:
                    self.__vacina_covid = v1
                else:
                    print("Erro!!! Tente novamente!")
            else:
                print('Primeira dose já foi aplicada!')
        else:
            print('Você precisa ter acima de 18 anos com comorbidade e/ou ter mais de 60 anos!!!')
            self.__descricao_comorbidade = "Sem comorbidades"

    def vacinardose2(self, datadose2=datetime.datetime.today()):
        if self.__vacina_covid != None:
            if self.__vacina_covid.datadose2 == None:
                self.__vacina_covid.datadose2 = datadose2.date() + datetime.timedelta(days=30)
                print("Segunda dose da vacina {} Data: {}" .format(self.__vacina_covid.tipo, self.__vacina_covid.datadose2))
            else:
                print('Você já tomou a segunda dose')
        else:
            print("você ainda não tomou a primeira dose!")
            self.__vacina_covid = "você não tomou a primeira dose ainda!!"