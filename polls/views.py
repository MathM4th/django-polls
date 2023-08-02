from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
  
def detail(request, question_id):
    return HttpResponse(f"Você está vendo os detalhes da questão {question_id}")


def results(request, question_id):
    return HttpResponse(f"Você está vendo os resultados da questão {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na questão {question_id}")