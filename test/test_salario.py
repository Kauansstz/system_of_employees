import pytest
def desconto_salario(salario):
    if salario < 0:
        raise ValueError("Salário não pode ser negativo")
    vt = 0.08
    va = 0.06
    desconto_va = salario * va
    salario_com_desconto = salario - desconto_va
    desconto_vt = salario_com_desconto * vt
    salario_final = salario_com_desconto - desconto_vt
    return salario_final



def test_desconto_salario():
    resultado = desconto_salario(1000)
    esperado = 1000 - (1000 * 0.06)  # desconto VA
    esperado = esperado - (esperado * 0.08)  # desconto VT
    assert resultado == esperado

def test_salario_negativo():
    with pytest.raises(ValueError):
        desconto_salario(-100)


def salario_pj(salario, horas):
    if salario < 0:
        raise ValueError("Salário não pode ser negativo")
    horas_trabalho = horas
    salario_final = horas_trabalho * salario
    return salario_final

def test_salario_pj():
    with pytest.raises(ValueError):
        salario_pj(-50, 160)
    assert salario_pj(50,160)