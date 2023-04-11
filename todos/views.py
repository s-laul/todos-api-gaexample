from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
   # The Main Query for the index route
   queryset = Todo.objects.all()
   # The serializer class for serializing output
   serializer_class = TodoSerializer
   # Optional permission class set permission level
   permission_classes = [permissions.AllowAny] 

# Create your views here.
