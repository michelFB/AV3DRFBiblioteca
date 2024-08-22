from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Livro, Categoria, Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer

# --------------------------- VIEWS DE LIVROS
@api_view(["GET","POST"])
@csrf_exempt
def livro_list_create(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def livro_detail(request, pk):
    livro = Livro.objects.get(pk=pk)

    if request.method == "GET":
        serializer = LivroSerializer(livro)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------- VIEWS DE CATEGORIAS
@api_view(["GET", "POST"])
@csrf_exempt
def categoria_list_create(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def categoria_detail(request, pk):
    categoria = categoria.objects.get(pk=pk)

    if request.method == "GET":
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------- VIEWS DE AUTORES


@api_view(["GET", "POST"])
@csrf_exempt
def autor_list_create(request):
    if request.method == "GET":
        autors = Autor.objects.all()
        serializer = AutorSerializer(autors, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def autor_detail(request, pk):
    autor = autor.objects.get(pk=pk)

    if request.method == "GET":
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
