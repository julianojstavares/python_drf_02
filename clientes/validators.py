import re
from validate_docbr import CPF


def validate_cpf(cpf):
    check = CPF()
    return check.validate(cpf)


def validate_nome(nome):
    return nome.isalpha()


def validate_rg(rg):
    return len(rg) == 9

def validate_celular(celular):
    """ Verifica se o celular é válido de acordo ao modelo 00 00000-0000"""
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, celular)
    return response
