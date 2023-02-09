"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import deletar_autor, listar_autor, detalhar_autor, cadastrar_autor, atualizar_autor, listar_noticia, deletar_noticia, cadastrar_noticia, atualizar_noticia, detalhar_noticia

urlpatterns = [
    path('autor/', listar_autor, name='listar_autores'),
    path('autor/<int:pk>', detalhar_autor, name='detalhar_autor'),
    path('autor/cadastrar', cadastrar_autor, name='cadastrar_autor'),
    path('autor/atualizar/<int:pk>', atualizar_autor, name='atualizar_autor'),
    path('autor/deletar/<int:pk>', deletar_autor, name='deletar_autor'),
    path('noticia/', listar_noticia, name='listar_noticias'),
    path('noticia/<int:pk>', detalhar_noticia, name='detalhar_noticia'),
    path('noticia/cadastrar', cadastrar_noticia, name='cadastrar_noticia'),
    path('noticia/atualizar/<int:pk>',
         atualizar_noticia, name='atualizar_noticia'),
    path('noticia/deletar/<int:pk>', deletar_noticia, name='deletar_noticia')
]
