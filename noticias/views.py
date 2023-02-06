from django.shortcuts import render
from .models import Autor

# Create your views here.

def index(request):
    return render(request, "index.html")

def listar(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "listar.html", context)

def detalhar(request, pk):
    autor = Autor.objects.get(pk=pk)
    context = {"autor": autor}
    return render(request, "detalhar.html", context)