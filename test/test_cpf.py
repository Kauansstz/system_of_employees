import pytest

def cpf(valor):
    if not int(valor.isdigit()):
        raise ValueError("O cpf tem que ter somente números")
    if len(valor) != 11:
        raise ValueError("O Cpf precisar ter 11 dígitos")
    return valor

def test_cpf_error():
    with pytest.raises(ValueError):
        cpf("0123456789")
    
def test_cpf_certo():
    assert cpf("01234567891")