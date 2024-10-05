from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Polls
from .forms import Inputforms
from .models import Question

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
        'details' : details
    }
    return HttpResponse(template.render(context, request))


#writing view for detail results and vote
# def detail(request, question_id):
#     try:
#     question = Question.objects.get(pk=question_id)
# except Question.DoesNotExist:
#     raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})
#     # return HttpResponse("You are looking at the question %s" %question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s."% question_id)

def form(request):
    context = {}
    context['form'] = Inputforms()
    return render(request, "index.html", context)

def index(request):
    latest_que_list = Question.objects.order_by("-pub_date")[:5]
    output = ",".join([q.question_text for q in latest_que_list])
    return HttpResponse(output)
    template = loader.get_template("polls/index.html")
    context = {
        "latest_que_list": latest_que_list,
    }
    return HttpResponse(template.render(context, request))