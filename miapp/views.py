from django.shortcuts import render, HttpResponse, redirect



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