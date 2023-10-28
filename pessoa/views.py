from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer, PessoaListSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PessoaListSerializer
        return PessoaSerializer