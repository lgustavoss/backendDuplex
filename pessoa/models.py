from django.db import models
from django.core.validators import EmailValidator

from .validators import validar_telefone, validar_cnpj_cpf


TIPO_PESSOA_CHOICES = (
    ('1', 'Pessoa Fisica'),
    ('2', 'Pessoa Juridica'),
)

class Pessoa(models.Model):
    # Nome fantasia da pessoa (255 caracteres no máximo)
    nome_fantasia = models.CharField(max_length=255, null=False, blank=False)
    # Razão social (255 caracteres no máximo, pode ser nulo)
    razao_social = models.CharField(max_length=255, null=True, blank=True)
    # Tipo de pessoa (Pessoa Física ou Pessoa Jurídica)
    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA_CHOICES, null=False, blank=False)
    # CPF ou CNPJ (11 a 18 caracteres)
    cnpj_cpf = models.CharField(max_length=18)
    # RG ou IE (50 caracteres no máximo, pode ser nulo)
    rg_ie = models.CharField(max_length=50, null=True, blank=True)
    # Data de nascimento (necessária para Pessoa Física)
    data_nascimento = models.DateField(blank=True, null=True)
    # Telefone (máximo de 15 caracteres, validado com a função)
    telefone = models.CharField(max_length=15, validators=[validar_telefone], blank=True)
    # Celular (máximo de 15 caracteres, validado com a função)
    celular = models.CharField(max_length=15, validators=[validar_telefone])
    # Email (validado com EmailValidator)
    email = models.EmailField(max_length=100, validators=[EmailValidator(message='Informe um email valido')])
    # Campos booleanos para indicar se a pessoa é: cliente, vendedor, transportadora ou fornecedor
    cliente = models.BooleanField(default=False, blank=True)
    vendedor = models.BooleanField(default=False, blank=True)
    transportadora = models.BooleanField(default=False, blank=True)
    fornecedor = models.BooleanField(default=False, blank=True)
    # Campo para indicar se o cadastro da pessoa está ativa (padrão True)
    ativo = models.BooleanField(default=True)
    # Data de cadastro (auto_now_add garante que seja preenchido automaticamente na criação)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    # Última alteração (auto_now garante que seja atualizado automaticamente)
    ultima_alteracao = models.DateTimeField(auto_now=True)
