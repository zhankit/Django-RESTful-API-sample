from django.db import models

# Create your models here.
class users_module(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  