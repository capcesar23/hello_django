from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(requets):
    return HttpResponse('Hello Word')