from django.contrib import admin
from .models import Autor, Noticia

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ["nome", "cpf", "email"]
    search_fields = ["nome", "email"]

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ["titulo", "data_pub", "autor"]
    search_fields = ["titulo", "autor__nome"]
    autocomplete_fields = ["autor"]


