from django.shortcuts import render
from .models import Autor

# Create your views here.

def index(request):

    autor = Autor.objects.get(pk=1)
    c =  {'autor':autor}
    return render(request, "index.html", c)