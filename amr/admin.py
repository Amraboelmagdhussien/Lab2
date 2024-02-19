from django.contrib import admin

# /* _______________Changed_______________ *
from .models import users,Student
# Register your models here.

admin.site.register(users)
admin.site.register(Student)