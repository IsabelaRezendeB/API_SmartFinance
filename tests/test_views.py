from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from smartfinance.models import Carteira, Usuario, Acao, Historico
from smartfinance.serializer import CarteiraSerializer, UsuarioSerializer, AcaoSerializer, HistoricoSerializer
from django.urls import reverse

class CarteiraViewSetTestCase(TestCase):
    def setUp(self):
        
        carteira = Carteira.objects.create(
            id = 1
        )

        self.client = APIClient()
        self.carteira_url = reverse('Carteiras-list')

    def test_resposta_get_carteira(self):
        """Verifica resposta do método GET de Carteira"""
        response = self.client.get(self.carteira_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_conteudo_get_carteira(self):
        """Verifica conteúdo do método GET de Carteira"""
        response = self.client.get(self.carteira_url)
        expected_data = CarteiraSerializer(Carteira.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_post_carteira(self):
        """Verifica método POST de Carteira"""
        data = {
            'id': 2
        }

        response = self.client.post(self.carteira_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Carteira.objects.filter(id = 2).exists())

class UsuarioViewSetTestCase(TestCase):
    def setUp(self):
        
        carteira = Carteira.objects.create(
            id=1
        )

        usuario = Usuario.objects.create(
            UID = "101",
            nome = "Isabela",
            sobrenome = "Rezende",
            carteira_id = carteira,
        )
        
        self.client = APIClient()
        self.usuario_url = reverse('Usuarios-list')
        self.usuario_url_parametro = reverse('Usuarios-detail', args=[str(usuario.UID)])

    def test_resposta_get_usuario(self):
        """Verifica resposta do método GET do Usuario"""
        response = self.client.get(self.usuario_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_conteudo_get_usuario(self):
        """Verifica conteúdo do método GET do Usuario"""
        response = self.client.get(self.usuario_url)
        expected_data = UsuarioSerializer(Usuario.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_post_usuario(self):
        """Verifica método POST do Usuario"""
        data = {
            'UID': "1010",
            'nome': 'Isabela',
            'sobrenome': 'Rezende',
            'carteira_id': 1
        }

        response = self.client.post(self.usuario_url, data, format='json')

        #if response.status_code != status.HTTP_201_CREATED:
        #    print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Usuario.objects.filter(nome='Isabela').exists())
    
    def test_put_usuario(self):
        """Verifica método PUT do Usuario"""
        updated_data = {
            'UID': "101",
            'nome': 'Gualter',
            'sobrenome': 'Machado',
            'carteira_id': 1
        }

        response = self.client.put(self.usuario_url_parametro, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertTrue(Usuario.objects.filter(UID = "101", nome = "Gualter", sobrenome = "Machado", carteira_id = 1).exists())
    
    def test_delete_usuario(self):
        """Verifica método DELETE do Usuario"""
        response = self.client.delete(self.usuario_url_parametro)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(UID="101")

class AcaoViewSetTestCase(TestCase):
    def setUp(self):
        
        carteira = Carteira.objects.create(
            id = 2
        )

        acao = Acao.objects.create(
            id = 1,
            identificador = "MGLU3",
            quantidade_total = 5,
            carteira_id = carteira
        )

        self.client = APIClient()
        self.acao_url = reverse('Acoes-list')
        self.acao_url_parametro = reverse('Acoes-detail', args=[str(acao.id)])

    def test_resposta_get_acao(self):
        """Verifica resposta do método GET de Ação"""
        response = self.client.get(self.acao_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_conteudo_get_acao(self):
        """Verifica conteúdo do método GET de Ação"""
        response = self.client.get(self.acao_url)
        expected_data = AcaoSerializer(Acao.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_post_acao(self):
        """Verifica método POST de Acao"""
        data = {
            'id': 2,
            'identificador': 'MGLU3',
            'quantidade_total': 5,
            'carteira_id': 2
        }

        response = self.client.post(self.acao_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Acao.objects.filter(identificador = "MGLU3").exists())
    
    def test_put_acao(self):
        """Verifica método PUT da Ação"""
        updated_data = {
            'id': 1,
            'identificador': 'PTR4',
            'quantidade_total': 6,
            'carteira_id': 2
        }

        response = self.client.put(self.acao_url_parametro, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertTrue(Acao.objects.filter(id = "1", identificador = "PTR4", quantidade_total = 6, carteira_id = 2).exists())
    
    def test_delete_acao(self):
        """Verifica método DELETE de Ação"""
        response = self.client.delete(self.acao_url_parametro)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Acao.DoesNotExist):
            Acao.objects.get(id=1)

class HistoricoViewSetTestCase(TestCase):
    def setUp(self):
        
        carteira = Carteira.objects.create(
            id = 2
        )

        historico = Historico.objects.create(
            id = 1,
            identificador = "MGLU3",
            data_entrada = "2023-05-31",
            quantidade = 5,
            carteira_id = carteira
        )

        self.client = APIClient()
        self.historico_url = reverse('Historico-list')
        self.historico_url_parametro = reverse('Historico-detail', args=[str(historico.id)])

    def test_resposta_get_historico(self):
        """Verifica resposta do método GET de Historico"""
        response = self.client.get(self.historico_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_conteudo_get_historico(self):
        """Verifica conteúdo do método GET de Historico"""
        response = self.client.get(self.historico_url)
        expected_data = HistoricoSerializer(Historico.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_post_historico(self):
        """Verifica método POST de Historico"""
        data = {
            'id': 2,
            'identificador': 'MGLU3',
            'data_entrada': '2023-05-31',
            'quantidade': 5,
            'carteira_id': 2
        }

        response = self.client.post(self.historico_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Historico.objects.filter(identificador = "MGLU3").exists())

    def test_put_historico(self):
        """Verifica método PUT de Histórico"""
        updated_data = {
            'id': 1,
            'identificador': 'PTR4',
            'data_entrada' : "2023-06-07",
            'quantidade': 6,
            'carteira_id': 2
        }

        response = self.client.put(self.historico_url_parametro, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertTrue(Historico.objects.filter(id = "1", identificador = "PTR4", data_entrada = "2023-06-07", quantidade = 6, carteira_id = 2).exists())
    
    def test_delete_historico(self):
        """Verifica método DELETE de Historico"""
        response = self.client.delete(self.historico_url_parametro)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Historico.DoesNotExist):
            Historico.objects.get(id=1)