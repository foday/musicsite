from django.shortcuts import render
from django.http import HttpResponse

# Create your views here & your functions
def index(request):
    return render(request, 'music/index.html')
    #HttpResponse("<h1>hello world</h1>")