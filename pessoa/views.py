from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pessoa
from .serializers import PessoaSerializer, PessoaListSerializer
from .filters import PessoaFilter


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    pagination_class = PageNumberPagination 
    filter_backends = [DjangoFilterBackend]
    filterset_class = PessoaFilter


    def list(self, request, *args, **kwargs):
        # Acesse o valor de 'page_size' na consulta
        page_size = request.query_params.get('page_size')
        
        if page_size:
            # Se 'page_size' foi especificado, use o valor fornecido
            self.paginator.page_size = int(page_size)

        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return PessoaListSerializer
        return PessoaSerializer

