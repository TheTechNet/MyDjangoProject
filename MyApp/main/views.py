from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")

def v1(request):
    return HttpResponse("View 1!")