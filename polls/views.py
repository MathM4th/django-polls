from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo! Esta é a página inicial do aplicativo")
    
def detail(request, question_id):
    return HttpResponse(f"Você está vendo os detalhes da questão {question_id}")


def results(request, question_id):
    return HttpResponse(f"Você está vendo os resultados da questão {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na questão {question_id}")