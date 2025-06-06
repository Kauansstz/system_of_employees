import pytest
import json

with open("info.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

def type_contract_clt(valor_nome):
    pessoa = next((p for p in base if p["nome"] == valor_nome), None)
    if pessoa and pessoa["Tipo de contrato"] in  ("CLT", "Kauan"):
        return f"{pessoa["nome"]}, {pessoa["salario"]}"
    else:
        raise ValueError("O colaborador é PJ")
    
    

def test_consult_contract():
    with pytest.raises(ValueError): 
        type_contract_clt("João")
    resultado = type_contract_clt("Kauan")
    assert "Kauan" in   resultado