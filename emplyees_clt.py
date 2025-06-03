import json

with open("info.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

class Employees:
    def __init__(self, name, salario):
        self.name = name
        self.contrato = base["Tipo de contrato"]
        self.salario = salario

    def descontos(self):
        VT = 8/100
        VA = 6/100

        desconto_va = self.salario * VA
        desconto_6 = self.salario - desconto_va

        desconto_vt = desconto_6 * VT
        salario_final = desconto_6 - desconto_vt
        return (f"Valor do salário é {salario_final}")

    def mostrar_salario(self):
        print(f'Salario com descontos: {self.descontos()}')

class Clt(Employees):
    def __init__(self, name, salario):
        super().__init__(name, salario)
        match name:
            case name if name in base["nome"]:
                encontrado = True
                match self.contrato:
                    case  self.contrato if  self.contrato == "CLT":
                        print(f"Colaborador: {name}")
                        print(f"Tipo de contrato: {base['Tipo de contrato']}")
                        print(f'Salário Base: {salario}')
                        self.mostrar_salario()
                    case _:
                        ...
            case _:
                print("Colaborador não existe")


l = Clt("João", 3000)