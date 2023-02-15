from django.shortcuts import render, HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(f"Welcome first polls app! question is : \n{output}")


def func(request):
    return HttpResponse("Hello, go to polls/")


def detail(request, question_id):
    return HttpResponse("You are looking at question %s " % question_id)


def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s " % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting at %s " % question_id)
