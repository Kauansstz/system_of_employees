import json

with open("info.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

class EmployeesPj:
    def __init__(self, name):
        self.pessoa = next((p for p in base if p["nome"] == name), None)
        if not self.pessoa:
            raise ValueError(f"Colaborador '{name}' não encontrado.")
        self.name = self.pessoa["nome"]
        self.contrato = self.pessoa["Tipo de contrato"]
        self.salario = float(self.pessoa["salario"])
        self.horas = self.pessoa["Horas de trabalho"]

    @property
    def nome(self):
        return self._name

    @nome.setter
    def nome(self, novo_nome):
        if  not novo_nome:
            raise ValueError("O nome inserido não existe")
        self._name = novo_nome
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo")
        self._salario = valor

    def calculo_salarial(self):
        horas_trabalhadas =  160

        salario_final = horas_trabalhadas * self.salario
        print(f"Valor do salário é {salario_final}")

class Pj(EmployeesPj):
    def __init__(self, name):
        try:
            super().__init__(name)
            if self.contrato == "PJ":
                print(f"Colaborador: {self.name}")
                print(f"Salário Base: {self.salario}")
                print(f"Tipo de contrato: {self.contrato}")
                self.calculo_salarial()
            else:
                print(f"{name} não é CLT.")
        except ValueError as e:
            print(e)


l = Pj("Kauan")