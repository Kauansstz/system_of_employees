import json
import os
from time import sleep

os.system('cls')
class Pessoa:
    def __init__(self):
        self._nome = ''
        self.idade = 0
        self._cpf = ''
        self.genero = ''
        self.salario = 0.0
        self.endereco = ''
        self.matricula = ''
        self.type_contract = 0
        self.horas = None
        self.valor_horas = None

    
class ValiedInfo(Pessoa):
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if  not novo_nome:
            raise ValueError("Nome não pode estar vazio")
        if not isinstance(novo_nome, str):
            raise ValueError("Nome deve ser somente por letras")
        self._nome = novo_nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 14:
            raise ValueError("O(a) colaborador(a) deve ter mais ou igual à 14 anos")
        if len(valor) <= 1:
            raise ValueError("A idade deve conter 2 digitos")
        self._idade = valor
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, valor):
        if not valor.isdigit():
            raise ValueError("A matrícula deve conter somente números")
        self._matricula = valor
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self,valor):
        if not valor.isdigit():
            raise ValueError("Digite apenas números (sem pontos ou traços)")
        if len(valor) != 11:
            raise ValueError("O CPF precisa ter exatamente 11 dígitos")
        self._cpf = valor
    
    @property
    def type_contract(self):
        return self._type_contract
    
    @type_contract.setter
    def type_contract(self, valor):
        if not valor.isdigit():
            raise ValueError("O tipo de contrato precisa ter somente números")
        if valor == 1:
            valor = "CLT"
        elif valor == 2: 
            valor = "PJ"
        else:
            print("Escolha algum das opções acima (1 ou 2)")
        self._type_contract = valor
        self.horas = None
    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self,valor):
        if self._type_contract.lower() == "CLT":
            self._horas = 44
        else: 
            self._horas= 160
        
    @property
    def valor_horas(self):
        return self._valor_horas

    @valor_horas.setter
    def valor_horas(self,valor):
        if self._type_contract == "clt":
            self._valor_horas = 0
        else: 
            self._valor_horas= valor

class Register(ValiedInfo):
    def solicit_info(self):
        print("Preencha algumas informações para prosseguir.")
        self.nome = input("Nome: ")
        self.idade = int(input("idade: "))
        self.cpf = int(input("cpf: "))
        self.genero = input("genero: ")
        self.salario = float(input("salario: "))
        self.endereco = input("endereco: ")
        self.matricula = int(input("matricula: "))
        self.type_contract = int(input("Tipo de contrato (1 - CLT | 2 - PJ): "))
        self.valor_horas = float(input("Valor da hora (obrigatório apenas para PJ): "))

    def message_success(self):
        print("Dados salvo com sucesso ✅")

    def message_error(self):
        print("Dados não salvos ❌")
    
    def review_info(self):
        print(f"Esses dados estão corretos ?\n Nome = {self.nome};\n Idade = {self.idade};\n CPF = {self.cpf};\n Genero = {self.genero};\n Salario = {self.salario};\n Endereço = {self.endereco};\n Matrícula = {self.matricula};\n Tipo = {self.type_contract};\n Horas de Trabalho: {self.horas};\n Valor de Horas Trabalhadas: {self.valor_horas}" )

class SaveRegister(Register):
    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "genero": self.genero,
            "salario": self.salario,
            "endereco": self.endereco,
            "matricula": self.matricula,
            "Tipo de contrato": self.type_contract,
            "Horas de trabalho": self.horas,
            "Valor de Horas trabalhadas": self.valor_horas
        }
    

    def confirm_info(self):
        self.review_info()
        sleep(1)
        confirm = input("As informações estão corretas? [S] ou [N]\nR: ").lower()

        match confirm:
            case 's':
                self.save_info(self.to_dict())
                self.message_success()
            case 'n':
                self.message_error()

    
    @staticmethod
    def save_info(dados):
        if os.path.exists("info.json") and os.path.getsize("info.json") > 0:
            with open("info.json", "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
        else:
            lista = []
        lista.append(dados)

        with open("info.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    registro = SaveRegister()
    registro.solicit_info()
    registro.confirm_info()