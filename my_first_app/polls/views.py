from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Polls
from .forms import Inputforms
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.
def home(request):
    home = loader.get_template('index.html')
    member = Polls.objects.all().values()
    context = {
        'home' : member,
    }
    return HttpResponse(home.render(context, request))

def details(request, id):
    template = loader.get_template('details.html')
    details = Polls.objects.get(id=id)
    context = {
        'details' : details,
    }
    return HttpResponse(template.render(context, request))

def vote(request, question_id):
    return HttpResponse("HI there!")

#updating the view to handle voting
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/details.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def question(request):
    # pub_date = Question.objects.values_list('pub_date')   
    # question = Question.objects.values_list('question_text') 

    ques = loader.get_template("question.html")
    question = Question.objects.all()
    context = {
        "question": question,
    }
    return render(request, 'question.html', context)

#make a view to get choice by question
def choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        "question" : question,
        "choices" : choices,
    }
    return render(request, 'choice.html', context)

