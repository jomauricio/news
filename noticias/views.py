from django.shortcuts import render, redirect
from .models import Autor, Noticia
from django.contrib.auth.decorators import login_required
from .forms import AutorForm, NoticiaForm

# Create your views here.

def index(request):
    
    # q = request.GET.get('q', '')
    noticias = Noticia.objects.all()[:5]
    autores = Autor.objects.all()[:5]
    noticias_destaque = noticias[:2]
    return render(request, "index.html", {'autores': autores, 'noticias': noticias, 'noticias_destaque': noticias_destaque})

def listar_autor(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "autor/listar.html", context)

def detalhar_autor(request, pk):
    autor = Autor.objects.get(pk=pk)
    context = {"autor": autor}
    return render(request, "autor/detalhar.html", context)

def cadastrar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AutorForm()
            return render(request, "autor/cadastrar.html", {'form': form})
    else:
        form = AutorForm()
        return render(request, "autor/cadastrar.html", {'form': form})

def atualizar_autor(request, pk):
    autor = Autor.objects.get(pk=pk)
    form = AutorForm(instance=autor)
    
    if request.method == "POST":
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "autor/atualizar.html", {'form': form})
    else:
        return render(request, "autor/atualizar.html", {'form': form})

def deletar_autor(request, pk):
    autor = Autor.objects.get(pk=pk)

    if autor:
        autor.delete()
        return redirect("/")
    else:
        return render(request, "autor/listar.html", {'msg': "Autor não encontrado"})

def listar_noticia(request):
    noticias = Noticia.objects.all()
    context = {"noticias": noticias}
    return render(request, "noticia/listar.html", context)

def detalhar_noticia(request, pk):
    noticia = Noticia.objects.get(pk=pk)
    context = {"noticia": noticia}
    return render(request, "noticia/detalhar.html", context)

@login_required
def cadastrar_noticia(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = NoticiaForm()
            return render(request, "noticia/cadastrar.html", {'form': form})
    else:
        form = NoticiaForm()
        return render(request, "noticia/cadastrar.html", {'form': form})

def atualizar_noticia(request, pk):
    noticia = Noticia.objects.get(pk=pk)
    form = NoticiaForm(instance=noticia)
    
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "noticia/atualizar.html", {'form': form})
    else:
        return render(request, "noticia/atualizar.html", {'form': form})

def deletar_noticia(request, pk):
    noticia = Noticia.objects.get(pk=pk)

    if noticia:
        noticia.delete()
        return redirect("noticias/noticia")
    else:
        return render(request, "noticia/listar.html", {'msg': "Noticia não encontrado"})