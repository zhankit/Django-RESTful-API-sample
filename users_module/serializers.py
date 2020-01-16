from rest_framework import serializers
from .models import users_module

class UsersModuleSerializer(serializers.ModelSerializer):
  class Meta:
    model = users_module
    fields = ('id','name','email')
