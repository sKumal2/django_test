#python shell script to get the data of Question and Choice
from polls.models import Question, Choice
Question.objects.all()
Choice.objects.all()

#python shell script to create a new question
from django.utils import timezone
q = Question(que_text="What's new?", pub_date=timezone.now())
q.save()

