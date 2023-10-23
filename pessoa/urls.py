from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet

#Objeto DefaultRouter para configurar as rotas automaticamente
router = DefaultRouter()
router.register(r'', PessoaViewSet) # 'pessoa' é o nome da rota

#urls
urlpatterns = [
    path("", include(router.urls)), #incluindo as rotas geradas pelo router
]
