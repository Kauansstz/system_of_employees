import pytest
import json

with open("info.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

def name_exits(valor_nome):
    nome = [p["nome"] for p in base if p["nome"] == valor_nome]
    if  not nome:
        raise ValueError("Nome não existe")
    nome = valor_nome
    

def test_consult_contract():
    with pytest.raises(ValueError): 
        name_exits("João")