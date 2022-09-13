from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .serializers import ContatoSerializer
from .models import Tarefa
from .models import Contato

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Tarefa.objects.all()

class ContatoView(viewsets.ModelViewSet):
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()