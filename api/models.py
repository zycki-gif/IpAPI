from django.db import models

# Create your models here.
class Company(models.Model):
    query = models.CharField(max_length=255)