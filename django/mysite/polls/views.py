from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.http import Http404
from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(f"Welcome first polls app! question is : \n{output}")

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request=request, template_name="polls/index.html", context=context)


def func(request):
    return HttpResponse("Hello, go to polls/")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request=request, template_name="polls/detail.html", context={"question": question})


def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s " % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting at %s " % question_id)
