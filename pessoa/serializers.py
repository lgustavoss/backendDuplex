from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

class PessoaListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome_fantasia = serializers.CharField()
    cnpj_cpf = serializers.CharField()

    class Meta:
        model = Pessoa