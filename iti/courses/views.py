from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_course(request):
    # return HttpResponse("<h1> <font color='blue'> Hello from courses <font> <h1> ")
    # html page contain hello from courses
    return render(request, "courseshome.html")
