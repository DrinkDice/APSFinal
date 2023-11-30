from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Filmes
from .serializers import FilmesSerializer

from rest_framework import viewsets
from . import serializers  # Import your serializers module
from . import models

#from rest_framework_simplejwt.tokens

import json

@api_view(['GET'])
def get_filmes(request):
    if request.method == 'GET':
        filmes = Filmes.objects.all()
        serializer = FilmesSerializer(filmes, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def get_by_filme(request, nome_filme):
    try:
        # Use nome_filme instead of pk
        if 'search' in request.query_params:
            filmes = Filmes.objects.filter(nome_filme__icontains=request.query_params['search'])
            serializer = FilmesSerializer(filmes, many=True)
            return Response(serializer.data)
        else:
            filme = Filmes.objects.get(nome_filme=nome_filme)
    except Filmes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilmesSerializer(filme)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = FilmesSerializer(filme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # Add DELETE operation
    if request.method == 'DELETE':
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    









# CRUD
# Acessos
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def filme_manager(request):
    if 'filme' in request.GET:
        try:
            nome_filme = request.GET['filme']
            filme = Filmes.objects.get(nome_filme=nome_filme)
            serializer = FilmesSerializer(filme)
            return Response(serializer.data)
        except Filmes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        # Check if a search query is provided in the request
        search_query = request.query_params.get('search', None)

        if search_query:
            # Perform a case-insensitive search by name
            filmes = Filmes.objects.filter(nome_filme__icontains=search_query)
        else:
            filmes = Filmes.objects.all()

        serializer = FilmesSerializer(filmes, many=True)
        return Response(serializer.data)


    # Criando Dados
    if request.method == 'POST':
        new_filme = request.data
        serializer = FilmesSerializer(data=new_filme)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # Update Dados
    if request.method == 'PUT':
        nome_filme = request.data['nome_filme']
        updated_filme = Filmes.objects.get(pk=nome_filme)
        print(request.data)
        serializer = FilmesSerializer(updated_filme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Delete Dados
    if request.method == 'DELETE':
        try:
            filme_to_delete = Filmes.objects.get(pk=request.data['nome_filme'])
            filme_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



    


class FilmesViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)  # Note the parentheses

    serializer_class = serializers.FilmesSerializer  
    queryset = models.Filmes.objects.all()




        



#def databaseEmDjango():

    #data = Filmes.objects.get(pk='nome_filme')

    #data = Filmes.objects.filter(data='data_lancamento')

    #data = Filmes.objects.exclude()

    #data.save()

    #data.delete()
