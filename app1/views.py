from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mumbai(request):
    return HttpResponse('<marquee><h1> Rock the party </h1><marquee>')
