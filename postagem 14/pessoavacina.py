from datetime import *
class Pessoa:
    def __init__(self, cpf, nome, data,lista, comorbidades=[]):
        self.__cpf = cpf
        self.nome = nome
        self.__data_nascimento = datetime.strptime(data,"%d/%m/%Y")
        self.__comorbidades = comorbidades
        self.__lista = lista
        self.idade = 0
        if type(lista)!= Comorbidade:
            print("Invalido")


    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return  self.__data_nascimento

    @property
    def comorbidades(self):
        return self.__comorbidades
    
    @property
    def lista(self):
        return self.__lista

    @comorbidades.setter
    def comorbidades(self, valor):
        self.__comorbidades = valor

    def getIdade(self):
        hoje = date.today()
        y = hoje.year - self.__data_nascimento.year
        if hoje.month < self.__data_nascimento.month or hoje.month == self.__data_nascimento.month and hoje.day < self.__data_nascimento.day:
            y -= 1
        return y
        
    def adcComorbidade(self,v):
        cmb = v in self.__lista.list_comorbidade
        if cmb == True:
            self.__comorbidades.append(v)
            print("Cormobidade registrada")
        else:
            print("Comorbidade inválida")
        

    def __str__(self):
        return "Cpf:"+str(self.__cpf)+"\n"+"Nome:"+str(self.nome)+"\n"+"Data de nascimento:"+str(self.__data_nascimento)+"\n"+"Comobirdades:"+str(self.__comorbidades)

class Comorbidade:
    def __init__(self, comorbidades_v=["Hipertensão arterial sistêmica", "Síndrome de Down", "Insuficiência cardíaca", "Diabetes"]):
        self.__comorbidades_v = comorbidades_v

    @property
    def list_comorbidade(self):
        return self.__list_comorbidade

    @list_comorbidade.setter
    def list_comorbidade(self, list_comorbidade):
        self.__list_comorbidade=self.list_comorbidade
    



class VacinaCovid:
    def __init__(self,numero,local,tipo,data_dose1,pessoa,dose2=None):
        self.__num_registro = numero
        self.local = local
        self.tipo = tipo
        if self.tipo == 1:
            self.tipo = "CoronaVac"
        elif self.tipo == 2:
            self.tipo = "Astrazeneca"
        elif self.tipo == 3:
            self.tipo = "Pfizer"
        self.__data_dose1 = datetime.strptime(data_dose1, "%d/%m/%Y")
        self.__data_dose2 = self.__data_dose1 + timedelta(days=61)
        self.__dose2 = dose2
        self.__comorbidades = pessoa.comorbidades
        if type(pessoa) == Pessoa:
            self.__pessoa = pessoa
        else:
            raise ValueError

    @property
    def num_registro(self):
        return self.__num_registro

    @property
    def data_dose1(self):
        return self.__data_dose1

    @property
    def dose2(self):
        return self.__dose2

    @property
    def data_dose2(self):
        return self.__data_dose2

    def vacinar2dose(self,data):
        self.__data_dose2 = datetime.strptime(data,"%d/%m/%Y")

    @property
    def pessoa(self):
        return self.__pessoa

    def __str__(self):
        return "Numero:"+str(self.__num_registro)+"\n"+"Local:"+str(self.local)+"\n"+"Tipo:"+str(self.tipo)+"\n"+"Pessoa:"+str(self.__pessoa)
    


class ControleVacina:
    def __init__(self):
        self.registroDeVacinas = []

    def incluirVacina(self,vacina):
        if type(vacina)==VacinaCovid:
            self.registroDeVacinas.append(vacina)
            print("Registro de Vacina cadastrado com sucesso!")
        else:
            print("Erro! Não foi possível cadastrar a informação.")


    def incluir2doseVacina(self,num_registro,data):
        Data1 = datetime.strptime(data, "%d/%m/%Y")
        achou = False
        for i in self.registroDeVacinas:
            if i.num_registro == num_registro:
                achou = True
                if i.dose2 == None:
                    if i.data_dose2 == Data1:
                        i.dose2 = 1
                    i.vacinar2dose(data)
                    print("A segunda dose foi cadastrada com sucesso!\nA data de aplicação é: {}".format(Data1))
                else:
                    print("A segunda dose já foi tomada.")
        if achou == False:
            print("Registro com a primeira vacinação não encontrado!")