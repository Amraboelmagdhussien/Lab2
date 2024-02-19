"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
# /* _______________Changed_______________ */
from amr.views import accept_user, signin, signup,logout, create_std, create_user, home, showdata ,delete_student, edit_student, about,contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",home ,name='home'),
    path("about/",about,name='about'),
    path("contact/",contact,name='contact'),
    path("signup/",signup,name='signup'),
    path("signin/",signin,name='signin'),
    path('create_user/', create_user, name='create_user'),
    path('accept_user/', accept_user, name='accept_user'),
    path('create_std/', create_std, name='create_std'),
    path("showdata/",showdata,name='showdata'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('edit_student/<int:student_id>/', edit_student, name='edit_student'),
    path('logout/', logout, name='logout'),


]