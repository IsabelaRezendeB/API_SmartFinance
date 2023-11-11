from django.db import models

class Usuario(models.Model):
    UID = models.CharField(max_length = 28, primary_key=True)
    nome = models.CharField(max_length = 100)
    sobrenome = models.CharField(max_length = 100)

    def __str__(self):
        return self.UID

class Acao(models.Model):
    nome = models.CharField(max_length = 100)
    data = models.DateField()
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Carteira(models.Model):
    usuario_UID = models.ForeignKey(Usuario, on_delete= models.PROTECT, related_name="carteira")
    acao_id = models.ForeignKey(Acao, on_delete= models.PROTECT, related_name="carteira")

    def __str__(self):
        return "%s - %s" %(self.usuario_UID, self.acao_id)
    