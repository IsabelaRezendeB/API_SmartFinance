from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from smartfinance.models import Usuario, Acao, Carteira
from smartfinance.serializer import UsuarioSerializer, AcaoSerializer, CarteiraSerializer
from rest_framework.response import Response

class UsuarioViewSet(viewsets.ModelViewSet):
    """Exibindo todas os usuarios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['carteira_id__id']
    filter_backends[1].search_param = 'q'

class AcaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as acoes"""
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['carteira_id__id']
    filter_backends[1].search_param = 'q'

class CarteiraViewSet(viewsets.ModelViewSet):
    """Exibindo todas as carteiras"""
    queryset = Carteira.objects.all()
    serializer_class = CarteiraSerializer