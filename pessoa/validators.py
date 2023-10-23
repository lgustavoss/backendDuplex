import re
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ

def validar_telefone(value):
    # Verificando se o numero de telefone está no formato esperado
    if not re.match(r'^\+\d{1,3} \d{4,16}$', value):
        raise ValidationError('O número de telefone deve estar no formato "+XX 123456789".')


def validar_cnpj_cpf(value):
    #removendo caracteres não numericos do valor
    cleaned_value = re.sub(r'[^0-9]', '', value)

    #verificando se o numero pertence a um cpf ou cnpj
    if len(cleaned_value) == 11:
        is_valid_cpf(cleaned_value)
    elif len(cleaned_value) == 14:
        is_valid_cnpj(cleaned_value)
    else:
        raise ValidationError('Favor informar um CPF ou CNPJ válido')
    

def is_valid_cpf(cpf):
    # Mascara o cpf antes de validar (usando a biblioteca validate_docbr)
    cpf_mask = CPF.mask(cpf)
    CPF.validate(cpf_mask)


def is_valid_cnpj(cnpj):
    # Mascara o cnpj antes de validar (usando a biblioteca validate_docbr)
    cnpj_mask = CNPJ.mask(cnpj)
    CNPJ.validate(cnpj_mask)