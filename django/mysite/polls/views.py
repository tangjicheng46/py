from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request=request, template_name="polls/results.html", context={"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Question.DoesNotExist):
        return render(request=request, template_name="polls/detail.html", context={"question": question})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))
