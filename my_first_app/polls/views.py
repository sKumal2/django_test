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


def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

   
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

#updating the view to handle voting
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
