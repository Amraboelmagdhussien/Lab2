from django.db import models

# Create your models here.

class users(models.Model):
    F_name=models.CharField(max_length=50)
    L_name=models.CharField(max_length=50)
    User_name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=20)


class Student(models.Model):
    id=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=50)
    S_Email=models.EmailField(max_length=20)
    Age=models.IntegerField()