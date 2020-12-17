from django.shortcuts import render
from django.http import HttpResponse

# Create your views here & your functions
def index(request):
    HttpResponse("<h1>hello world</h1>")