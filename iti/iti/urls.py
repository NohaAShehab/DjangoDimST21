"""iti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from students.views import say_hello, listStudents, helloStudent, viewstudent
from courses.views import hello_course

urlpatterns = [
    path('admin/', admin.site.urls),
    ## define url

    ### define new route staff
    # path('welcome', sayWelcome),
    # path('image', displayimage),
    # path('staff/<int:staff_id>', staffprofile)

    ## define staff/urls.py
    path("staff/", include("staff.urls")),

    ### define courses
    path("courses/", include("courses.urls")),

    ## define students
    path("students/", include("students.urls")),

    ### define products urls
    path("products/", include("products.urls")),



]
