from django.shortcuts import render, redirect
from .models import Student
from amr.models import users, Student

# Create your views here.

def home(request):
    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request, 'amr/signup.html')
    return render(request, 'amr/home.html')

def about(request):
    return render(request, 'amr/about.html')

def contact(request):
    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request, 'amr/signup.html')
    return render(request, 'amr/contact.html')

def signup(request):
    return render(request, 'amr/signup.html')

def signin(request):
    return render(request, 'amr/signin.html')

def create_user(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass']
        user = users.objects.create(
            F_name=first_name,
            L_name=last_name,
            User_name=username,
            Email=email,
            Password=password
        )
        return redirect('signin') 
    else:
        return render(request, 'amr/signup.html')

def accept_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = users.objects.filter(Email=email, Password=password).first()
        if user is not None:
            request.session['user_email'] = user.Email
            request.session['userpass'] = user.Password
            return redirect('home')
        else:
            return render(request, 'amr/signup.html')

def create_std(request):
    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request, 'amr/signup.html')
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        email = request.POST.get('email')
        age = request.POST.get('age')
        student = Student.objects.create(
            s_name=first_name,
            Age=age,
            S_Email=email,
        )
        return redirect('showdata') 
    else:
        return redirect('contact')  

def showdata(request):
    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request, 'amr/signup.html')
    students = Student.objects.all()
    return render(request, 'amr/show_users.html', {'students': students})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id).delete()
    return redirect('showdata')

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.s_name = request.POST.get('fname')
        student.S_Email = request.POST.get('email')
        student.Age = request.POST.get('age')
        student.save()
        return redirect('showdata') 
    return render(request, 'amr/edit_student.html', {'student': student})

def logout(request):
    request.session.clear()
    return render(request, 'amr/signup.html')
