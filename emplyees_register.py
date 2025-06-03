import json
from time import sleep
    
class Pessoa:
    def __init__(self, name, idade, cpf, genero, salario, endereco, matricula, type_contract):
        self.name = name
        self.idade = idade
        self.cpf = cpf
        self.genero = genero
        self.salario = salario
        self.endereco = endereco
        self.matricula = matricula
        self.type_contract = type_contract

    def get_nome(self):
        return self.name

    def get_idade(self):
        return self.idade
    
    def get_cpf(self):
        return self.cpf
    
    def get_genero(self):
        return self.genero
    
    def get_salario(self):
        return self.salario
    
    def get_endereco(self):
        return self.endereco
    
    def get_matricula(self):
        return self.matricula
    
class Register(Pessoa):
    def solicit_info(self):
        print("Preencha algumas informações para prosseguir.")
        self.name = input("Nome: ")
        self.idade = input("idade: ")
        self.cpf = input("cpf: ")
        self.genero = input("genero: ")
        self.salario = input("salario: ")
        self.endereco = input("endereco: ")
        self.matricula = input("matricula: ")
        self.type_contract = input("Tipo de contrato: ")

    def to_dict(self):
        return {
            "nome": self.name,
            "idade": self.idade,
            "cpf": self.cpf,
            "genero": self.genero,
            "salario": self.salario,
            "endereco": self.endereco,
            "matricula": self.matricula,
            "Tipo de contrato": self.type_contract
        }

    def confirm_info(self):
        response = print(f"Esses dados estão corretos ?\n Nome = {self.name};\n Idade = {self.idade};\n CPF = {self.cpf};\n Genero = {self.genero};\n Salario = {self.salario};\n Endereço = {self.endereco};\n Matrícula = {self.matricula}; Tipo = {self.type_contract}")
        sleep(1)
        confirm = input("As informações estão corretas? [S] ou [N]\nR: ").lower()

        match confirm:
            case 's':
                self.save_info(self.to_dict())
                print("Dados salvo com sucesso ✅")
            case 'n':
                print("Dados não salvos")
    @staticmethod
    def save_info(dados):
        with open("info.json", "a", encoding="utf8") as arquivo:
            json.dump(dados, arquivo,ensure_ascii=False)

pessoa = Register("João", 25, "123.456.789-00", "Masculino", 3000, "Rua A, 123", "001", "PJ")
pessoa.confirm_info()
