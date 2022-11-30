from django.db import models

# Create your models here.

class Snippet(models.Model):
    name = models.CharField(max_length=20,null=True)
    roll = models.IntegerField(null=True)
    sub = models.CharField(max_length=20,null=True)