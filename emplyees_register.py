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
        self.type_contract = ''
        self.horas = None


class Register(Pessoa):
    def solicit_info(self):
        print("Preencha algumas informações para prosseguir.")
        self.nome = input("Nome: ")
        self.idade = input("idade: ")
        self.cpf = input("cpf: ")
        self.genero = input("genero: ")
        self.salario = input("salario: ")
        self.endereco = input("endereco: ")
        self.matricula = input("matricula: ")
        self.type_contract = input("Tipo de contrato: ")
        
    

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
            "Horas de trabalho": self.horas
        }

    def confirm_info(self):
        print(f"Esses dados estão corretos ?\n Nome = {self.nome};\n Idade = {self.idade};\n CPF = {self.cpf};\n Genero = {self.genero};\n Salario = {self.salario};\n Endereço = {self.endereco};\n Matrícula = {self.matricula};\n Tipo = {self.type_contract};\n Horas de Trabalho: {self.horas}" )
        sleep(1)
        confirm = input("As informações estão corretas? [S] ou [N]\nR: ").lower()

        match confirm:
            case 's':
                self.save_info(self.to_dict())
                print("Dados salvo com sucesso ✅")
            case 'n':
                print("Dados não salvos ❌")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if  not novo_nome:
            raise ValueError("Nome não pode estar vazio")
        self._nome = novo_nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self,valor):
        if not valor.isdigit():
            raise ValueError("O CPF precisa somente números")
        if len(valor) != 11:
            raise ValueError("O CPF precisa ter exatamente 11 dígitos")
        self._cpf = valor
    
    @property
    def type_contract(self):
        return self._type_contract

    @type_contract.setter
    def type_contract(self, valor):
        self._type_contract = valor
        self.horas = None
    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self,valor):
        if self._type_contract == "clt":
            self._horas = 44
        else: 
            self._horas= 0
        
    

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
    registro = Register()
    registro.solicit_info()
    registro.confirm_info()