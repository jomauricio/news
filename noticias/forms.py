from django import forms
from .models import Autor, Noticia
from django.contrib.auth.forms import UserCreationForm

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'cpf', 'data_nascimento']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'data_pub', 'img', 'autor']

class MyUserCreationForm(UserCreationForm):
    pass



