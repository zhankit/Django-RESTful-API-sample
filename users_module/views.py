from django.shortcuts import render
from rest_framework import viewsets
from .models import users_module
from .serializers import UsersModuleSerializer

# Create your views here.
class UsersView(viewsets.ModelViewSet):
  queryset = users_module.objects.all()
  serializer_class = UsersModuleSerializer