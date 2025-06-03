from emplyees_register import Pessoa
class Clt(Pessoa):
    def __init__(self, name, salario):
        super().__init__(name, salario)

    def vale_transporte_valor(self):
        self.vale_transporte = 8
    
    

    def vale_alimentacao_valor(self):
        self.vale_alimentacao = 6
    
    def calculo_salario(self):
        nome = self.nome
        VA = self.vale_alimentacao
        VT = self.vale_transporte
        salario = self.salario

        result = salario - VA - VT
