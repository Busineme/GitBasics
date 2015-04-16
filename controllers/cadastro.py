from django.shortcuts import render_to_response
from models.livro import Livro
from models.autor import Autor

def home(request):
    return render_to_response('home.html')

def cadastro(request):
    lista_autores = Autor.objects.all()

    return render_to_response('cadastro.html', {'autores': lista_autores})

def cadastrar_livro(request):
    livro = Livro()
    livro.nome = request.GET['nome']
    livro.autor_id = request.GET['autor']
    livro.save()

    return render_to_response('home.html')
