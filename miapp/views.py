from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article


def index(request):   
    return render(request,'index.html',{
        'title':'Página de Inicio',
        'mi_variable':'Soy un dato que esta en la vista'
    })
 
def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('/')

    return render(request, 'pagina.html')

def contacto(request, nombre="Julio", apellido="Corrales"):
    return render(request, 'contacto.html')

def crear_articulo(request):

    articulo = Article(
        title = 'Primer articulo',
        content = 'Contenido del articulo',
        public = True
    )

    articulo.save()

    return HttpResponse(f"Articulo creado {articulo.title} {articulo.content}")

def articulo(request):

    articulo = Article.objects.get(pk=4)

    return HttpResponse(f"Articulo: {articulo.title}")

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.content =  "Este es el contenido modificado"

    articulo.save()

    return HttpResponse(f"Articulo editado : {articulo.title} - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all()

    return render(request, 'articulos.html',{'articulos': articulos})

def borrar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')