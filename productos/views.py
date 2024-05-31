from django.shortcuts import render
from .models import Producto

# Create your views here.
productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})