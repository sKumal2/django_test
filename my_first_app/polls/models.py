from django.db import models
from django.utils import timezone
import datetime
from django.shortcuts import render, get_object_or_404

# Create your models here.
class Polls(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)

class Question(models.Model):
    que_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("published date")
    def __str__(self):
        return self.que_text
    def was_pub_rec(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

def Vote(request, que_id):
    que = get_object_or_404(Question, pk = que_id)
    return render(request, 'polls/vote.html', {'question', que})

      

