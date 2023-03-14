from django.forms import ModelForm
from .models import Autor, Noticia

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'cpf', 'data_nascimento']

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'data_pub', 'img', 'autor']



