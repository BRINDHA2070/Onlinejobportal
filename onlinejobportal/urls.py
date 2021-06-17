"""onlinejobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from jobportal.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('recruiter/',recruiter,name="recruiter"),
    path('admin_recruiter/',admin_recruiter,name="admin_recruiter"),
    path('signupuser/',signupuser,name="signupuser"),
    path('login_user', Login, name="login_user"),
    path('logout_admin/', Admin_logout, name="logout_admin"),
    path('logout_user/', logout_user, name="logout_user"),
    path('recruiter_logout/', recruiter_logout, name="recruiter_logout"),
    path('login_admin/', Admin_Login, name="login_admin"),
    path('admin_home/', Admin_home, name="admin_home"),
    path('recruiter_home/', recruiter_home, name="recruiter_home"),
    path('user_home/', user_home, name="user_home"),
    path('view_newrecruiter/', view_newrecruiter, name="view_newrecruiter"),
    path('edit_profile/', Edit_profile, name="edit_profile"),
    path('useredit_profile/', UserEdit_profile, name="useredit_profile"),
    path('add_job/', add_job, name="add_job"),
    path('view_user/', view_user, name="view_user"),
    path('recruiter_login/', Recruiter_Login, name="recruiter_login"),
    path('assign_status/<int:pid>', Assign_status, name="assign_status"),
    path('change_password/', Change_Password, name="change_password"),
    path('change_password_recruiter/', RecruiterChange_Password, name="change_password_instruct"),
    path('contact', Contact, name="contact"),


]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
