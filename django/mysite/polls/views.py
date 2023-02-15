from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Welcome first polls app!")


def func(request):
    return HttpResponse("Hello, go to polls/")
