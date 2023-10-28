import re
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ



def validar_telefone(value):
    # Verificando se o numero de telefone está no formato esperado
    if not re.match(r'^\+\d{1,3} \d{4,16}$', value):
        raise ValidationError('O número de telefone deve estar no formato "+XX 123456789".')

# Validando CPF ou CNPJ
def validar_cnpj_cpf(value):
    # Removendo caracteres não numéricos do valor
    cleaned_value = re.sub(r'[^0-9]', '', value)

    # Verificando se o número pertence a um CPF ou CNPJ
    if len(cleaned_value) == 11:
        cpf_instance = CPF()
        if not cpf_instance.validate(cleaned_value):
            raise ValidationError('CPF inválido')
    elif len(cleaned_value) == 14:
        cnpj_instance = CNPJ()
        if not cnpj_instance.validate(cleaned_value):
            raise ValidationError('CNPJ inválido')
    else:
        raise ValidationError('Favor informar um CPF ou CNPJ válido')