from django.contrib import admin
from django.urls import path
from staff.views import sayWelcome, displayimage, staffprofile, \
    testfunction,staffindex, stafflist,getstaffprofile,createStaff,\
    deleteProfile, editProfile,updateProfile


# path('staff/<int:staff_id>', staffprofile)
urlpatterns = [
    path('welcome', sayWelcome),
    path('image', displayimage),
    # path('<int:staff_id>', staffprofile),
    path('test', testfunction),
    path('index', staffindex),
    path('staffindex', stafflist, name="list_staff"),
    path('<int:staff_id>', getstaffprofile, name="view_staff"),
    path('create', createStaff, name="createstaff"),
    path("<int:staff_id>/delete", deleteProfile, name="delete_staff"),
    path("<int:staff_id>/edit", editProfile, name="edit_staff"),
    path("<int:staff_id>/update", updateProfile, name="update_staff"),



]
