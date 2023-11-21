from django.test import TestCase
from smartfinance.models import Carteira, Usuario, Acao, Historico
from smartfinance.serializer import CarteiraSerializer, UsuarioSerializer, AcaoSerializer, HistoricoSerializer

class CarteiraSerializerTestCase(TestCase):

    def setUp(self):

        self.carteira = Carteira(
            id = 1
        )

        self.serializer = CarteiraSerializer(instance = self.carteira)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Carteira estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Carteira está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.carteira.id)

class UsuarioSerializerTestCase(TestCase):

    def setUp(self):

        self.carteira = Carteira(
            id = 1
        )

        self.usuario = Usuario(
            UID = "1",
            nome = "Isabela",
            sobrenome = "Rezende",
            carteira_id = self.carteira
        )
        self.serializer = UsuarioSerializer(instance = self.usuario)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Usuario estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['UID', 'nome', 'sobrenome', 'carteira_id']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Usuario está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['UID'], self.usuario.UID)
        self.assertEqual(data['nome'], self.usuario.nome)
        self.assertEqual(data['sobrenome'], self.usuario.sobrenome)
        self.assertEqual(data['carteira_id'], self.usuario.carteira_id.id)

class AcaoSerializerTestCase(TestCase):

    def setUp(self):

        self.carteira = Carteira(
            id = 1
        )

        self.acao = Acao(
            id = 1,
            identificador = "MGLU3",
            quantidade_total = 5,
            carteira_id = self.carteira
        )

        self.serializer = AcaoSerializer(instance = self.acao)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Acao estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'identificador', 'quantidade_total', 'carteira_id']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Acao está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.acao.id)
        self.assertEqual(data['identificador'], self.acao.identificador)
        self.assertEqual(data['quantidade_total'], self.acao.quantidade_total)
        self.assertEqual(data['carteira_id'], self.acao.carteira_id.id)

class HistoricoSerializerTestCase(TestCase):

    def setUp(self):

        self.carteira = Carteira(
            id = 1
        )

        self.historico = Historico(
            id = 1,
            identificador = "MGLU3",
            data_entrada = "2023/05/31",
            quantidade = 5,
            carteira_id = self.carteira
        )

        self.serializer = HistoricoSerializer(instance = self.historico)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Historico estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'identificador', 'data_entrada', 'quantidade', 'carteira_id']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Historico está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.historico.id)
        self.assertEqual(data['identificador'], self.historico.identificador)
        self.assertEqual(data['data_entrada'], self.historico.data_entrada)
        self.assertEqual(data['quantidade'], self.historico.quantidade)
        self.assertEqual(data['carteira_id'], self.historico.carteira_id.id)