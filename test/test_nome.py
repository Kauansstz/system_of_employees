import json

with open("info.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

def consulta_user(nome):
    nome = [p["nome"] for p in base]
    assert "Kauan" in nome

def test_consulta_user():
    consulta_user("Kauan")