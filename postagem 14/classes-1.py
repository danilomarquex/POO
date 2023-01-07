from datetime import *
class Pessoa:
    def __init__(self,cpf,nome,data,comorb_list,comorbidades=[]):
        self.__cpf = cpf
        self.nome = nome
        self.__data_nascimento = datetime.strptime(data,"%d/%m/%Y")
        self.__comorb_list = comorb_list
        self.__comorbidades = comorbidades
        self.idd = 0

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def comorb_list(self):
        return self.__comorb_list

    @property
    def comorbidades(self):
        return self.__comorbidades

    @comorbidades.setter
    def comorbidades(self,valor):
        self.__comorbidades=valor

    def getIdade(self):
        hoje = date.today()
        y = hoje.year - self.__data_nascimento.year
        if hoje.month < self.__data_nascimento.month or hoje.month == self.__data_nascimento.month and hoje.day < self.__data_nascimento.day:
            y -= 1
        self.idd = y
        return y


    def adicionarComorbidade(self, v):
        cmb = v.upper() in self.__comorb_list.comorbidades_v
        if cmb == True:
            self.__comorbidades.append(v)
            print('Cormobidade Adicionada!')
        else:
            print('Comorbidades não Aceita!')


class VacinaCovid:
    def __init__(self,numero,local,tipo,data_dose1,pessoa):
        self.__num_registro = numero
        self.local = local
        self.tipo = tipo
        self.__data_dose1 = datetime.strptime(data_dose1,"%d/%m/%Y")
        self.__data_dose2 = self.__data_dose1 + timedelta(days=61)
        self.__comorbidades = pessoa.comorbidades
        if type(pessoa)==Pessoa:
            self.__pessoa = pessoa
        else:
            raise ValueError

    @property
    def data_dose1(self):
        return self.__data_dose1

    @property
    def num_registro(self):
        return self.__num_registro

    @property
    def data_dose2(self):
        return self.__data_dose2

    @property
    def pessoa (self):
        return self.__pessoa

    @property
    def comorbidades(self):
        return self.__comorbidades

    def vacinar2dose(self,data):
        self.__data_dose2 = datetime.strptime(data,"%d/%m/%Y")
        # implementar os decoradores

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
        dt1 = datetime.strptime(data,"%d/%m/%Y")
        achou = False
        for i in self.registroDeVacinas:
            if i.num_registro == num_registro:
                achou=True
                #if testar se a data é dois meses maior que a data da 1a vacina
                if i.data_dose2 == dt1:
                    i.vacinar2dose(data)
                    print("SEGUNDA DOSE CADASTRADA")
                else:
                    print('ERRO!A SEGUNDA DOSE SÓ PODE SER TOMADA 2 MESES APÓS A PRIMEIRA !')
        if achou==False:
            print("PRIMEIRA DOSE NÃO REGISTRADA!")

    def excluirVacina(self,vacina):
        if type(vacina) == VacinaCovid:
           self.registroDeVacinas.remove(vacina)
           print("Registro exclido com sucesso!")
        else:
            print("Não foi possível excluir o resgistro")

    def relatorio(self):
        t = len(self.registroDeVacinas)
        pessoasx = 0
        for i in self.registroDeVacinas:
            if len(i.comorbidades) >= 1:
                if i.pessoa.idd >= 40:
                    pessoasx += 1
                elif i.pessoa.idd == 0:
                    id = i.pessoa.getIdade()
                    if id >= 40:
                        pessoasx += 1
        porcent = (pessoasx/t)*100
        print('Total de Pessoas com mais de 40 anos, possui comorbidade e já tomou a 1ª Dose : {}\nPorcentagem : {}%'.format(pessoasx,porcent))
class Comorbidades:
    def __init__(self,comorbidades_v = ['HIV','TUBERCULOSE','OBESIDADE MORBITA, DIABETES']):
        self.__comorbidades_v = comorbidades_v

    @property
    def comorbidades_v(self):
        return self.__comorbidades_v

    @comorbidades_v.setter
    def comorbidades_v(self,valor):
        self.__comorbidades_v.append(valor)
        