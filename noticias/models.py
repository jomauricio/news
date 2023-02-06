from django.db import models

# Create your models here.

class Autor(models.Model):

    nome = models.CharField(max_length=250)
    email = models.EmailField()
    cpf = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.nome, self.email)