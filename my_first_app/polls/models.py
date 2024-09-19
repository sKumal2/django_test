from django.db import models

# Create your models here.
class Polls(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)