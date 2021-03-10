from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from miapp.forms import FormArticle
from django.contrib import messages

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

def save_articulo(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse(f"Articulo creado {articulo.title} {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

    return HttpResponse(f"Articulo creado {articulo.title} {articulo.content}")

def create_article(request):

    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            #Crear mensaje flash
            messages.success(request, 'El articulo ha sido guardado correctamente')
            
            return redirect('articulos')
        else:
            return render(request,'create_full_article.html',{ 'form':formulario })
    
    else:    
        formulario = FormArticle()

        return render(request, 'create_full_article.html', {'form': formulario})

def articulo(request):

    articulo = Article.objects.get(pk=4)

    return HttpResponse(f"Articulo: {articulo.title}")

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.content =  "Este es el contenido modificado"

    articulo.save()

    return HttpResponse(f"Articulo editado : {articulo.title} - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all().order_by('-id')

    return render(request, 'articulos.html',{'articulos': articulos})

def borrar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')