from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=12)

    def get_absolute_url(self):
        return reverse("password")
    
    