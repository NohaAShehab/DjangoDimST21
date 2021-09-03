

from django.urls import path, include
from courses.views import hello_course

# path('courses/', hello_course),


urlpatterns = [

    path('hellocourse', hello_course),

]
