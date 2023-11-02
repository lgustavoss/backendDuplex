import django_filters
from .models import Pessoa

class PessoaFilter(django_filters.FilterSet):
    nome_fantasia__icontains = django_filters.CharFilter(field_name='nome_fantasia', lookup_expr='icontains')

    class Meta:
        model = Pessoa
        fields = ['nome_fantasia__icontains']
