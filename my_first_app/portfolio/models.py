from django.db import models

# Create your models here.
class portfolio(models.Model):
    firstname = models.CharField()
    lastname = models.CharField()