from django.urls import path
from students.views import listStudents, viewstudent

urlpatterns = [
    path('', listStudents),
    path('<stdname>', viewstudent),
]
