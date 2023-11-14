from django.db import models

class Carteira(models.Model):

    def __str__(self):
        return self.id

class Usuario(models.Model):
    UID = models.CharField(max_length = 28, primary_key=True)
    nome = models.CharField(max_length = 100)
    sobrenome = models.CharField(max_length = 100)
    carteira_id = models.ForeignKey(Carteira, on_delete= models.PROTECT, related_name="usuario")

    def __str__(self):
        return "%s - %s" %(self.UID, self.carteira_id)

class Acao(models.Model):
    identificador = models.CharField(max_length = 100)
    data_entrada = models.DateField()
    quantidade = models.IntegerField()
    carteira_id = models.ForeignKey(Carteira, on_delete= models.PROTECT, related_name="acao")

    def __str__(self):
        return self.nome
    