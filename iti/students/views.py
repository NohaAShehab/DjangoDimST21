from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


### when this file called , repond with
### http -
def say_hello(request):
    return HttpResponse("Hello from student")


def listStudents(request):
    # return HttpResponse("List students route")
    students = ['dana', 'Ahmed', 'Abdulrahman', 'Noha']
    # create dictionay ---> students
    context = {"students": students}
    return render(request, "studentslist.html", context)


def helloStudent(request, studentname):
    return HttpResponse(f"Hiiii student {studentname}")


def viewstudent(request, stdname):
    # return HttpResponse(f" hellllo from click ya {stdname}")

    ## send request parameter to the html page
    # render (request, htmlpage, parameters in form of dictionary)
    context = {"studentname": stdname}
    # return render(request, "studentprofile.html", {"studentname": stdname})
    return render(request, "studentprofile.html", context)




