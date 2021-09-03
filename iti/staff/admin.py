from django.contrib import admin

# Register your models here to be added to the admin

from staff.models import Staff, Departments

admin.site.register(Staff)

admin.site.register(Departments)


