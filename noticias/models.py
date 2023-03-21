from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Autor(models.Model):

    nome = models.CharField("Nome", max_length=250, blank=True)
    email = models.EmailField("Email", blank=True)
    cpf = models.CharField("CPF", max_length=15, blank=True)
    data_nascimento = models.DateField("Data de nascimento", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome)
    
    class Meta:
        verbose_name_plural = "Autores"

class Noticia(models.Model):

    titulo = models.CharField("Titulo", max_length=100)
    conteudo = models.TextField("Conteudo")
    data_pub = models.DateField("Data de publicação")
    img = models.ImageField("Imagem", upload_to='imagens', null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='noticias', verbose_name="Autor")

    def __str__(self):
        return "{}".format(self.titulo)

    class Meta:
        verbose_name_plural = "Noticias"