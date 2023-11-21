from django.test import TestCase
from smartfinance.models import Carteira, Usuario, Acao, Historico

class CarteiraModelTestCase(TestCase):

    def setUp(self):
        self.carteira = Carteira(
            id = 1
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Carteira"""
        self.assertEqual(self.carteira.id, 1)

class UsuarioModelTestCase(TestCase):

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
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Usuario"""
        self.assertEqual(self.usuario.UID, "1")
        self.assertEqual(self.usuario.nome, 'Isabela')
        self.assertEqual(self.usuario.sobrenome, 'Rezende')
        self.assertEqual(self.usuario.carteira_id.id, 1)

class AcaoModelTestCase(TestCase):

    def setUp(self):

        self.carteira = Carteira(
            id = 1
        )

        self.acao = Acao(
            identificador = "MGLU3",
            quantidade_total = 5,
            carteira_id = self.carteira
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Acao"""
        self.assertEqual(self.acao.identificador, "MGLU3")
        self.assertEqual(self.acao.quantidade_total, 5)
        carteira = self.acao.carteira_id
        self.assertEqual(carteira.id, 1)

class HistoricoModelTestCase(TestCase):

    def setUp(self):

        self.carteira = Carteira(
            id = 1
        )

        self.historico = Historico(
            identificador = "MGLU3",
            data_entrada = "2023/05/31",
            quantidade = 5,
            carteira_id = self.carteira
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Historico"""
        self.assertEqual(self.historico.identificador, "MGLU3")
        self.assertEqual(self.historico.data_entrada, "2023/05/31")
        self.assertEqual(self.historico.quantidade, 5)
        carteira = self.historico.carteira_id
        self.assertEqual(carteira.id, 1)
