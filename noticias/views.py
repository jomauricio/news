from django.shortcuts import render, redirect
from .models import Autor

from .forms import AutorForm

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

def cadastrar(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AutorForm()
            return render(request, "cadastrar.html", {'form': form})
    else:
        form = AutorForm()
        return render(request, "cadastrar.html", {'form': form})

def atualizar(request, pk):
    autor = Autor.objects.get(pk=pk)
    form = AutorForm(instance=autor)
    
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "atualizar.html", {'form': form})
    else:
        return render(request, "atualizar.html", {'form': form})

def deletar(request, pk):
    autor = Autor.objects.get(pk=pk)

    if autor:
        autor.delete()
        return redirect("/autores")
    else:
        return render(request, "listar.html", {'msg': "Autor não encontrado"})
