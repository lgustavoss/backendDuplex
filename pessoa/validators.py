import re
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ

# Validando telefone
def validar_telefone(value):
    # Verificando se o número de telefone está no formato esperado
    if not re.match(r'^\+\d{1,3} \d{4,16}$', value):
        raise ValidationError('O número de telefone deve estar no formato "+XX 123456789".')

# Aplicando a máscara no CPF ou CNPJ
def formatar_cnpj_cpf(value):
    # Removendo caracteres não numéricos do valor
    cleaned_value = re.sub(r'[^0-9]', '', value)

    if len(cleaned_value) == 11:
        return '{}.{}.{}-{}'.format(cleaned_value[:3], cleaned_value[3:6], cleaned_value[6:9], cleaned_value[9:])
    elif len(cleaned_value) == 14:
        return '{}.{}.{}/{}-{}'.format(cleaned_value[:2], cleaned_value[2:5], cleaned_value[5:8], cleaned_value[8:12], cleaned_value[12:])
    else:
        raise ValidationError('Favor informar um CPF ou CNPJ válido')

# Validando CPF ou CNPJ com a máscara
def validar_cnpj_cpf(value):
    # Formate o valor com a máscara
    value = formatar_cnpj_cpf(value)
    
    # Remova a máscara para validação
    cleaned_value = re.sub(r'[^0-9]', '', value)

    # Verifique se o número pertence a um CPF ou CNPJ
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
