from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import datetime
from datetime import date
from .models import *
from datetime import datetime
# Create your views here.

def Home(request):
    return render(request,'user_home.html')
def signupuser(request):
    error = False
    if request.method == 'POST':
        u = request.POST['uname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        user = User.objects.create_user(email=e,username=u, password=p,last_name=l)
        sign = SignupUser.objects.create(user=user,mobile=con,image=i,gender=gen,type="customer")
        error = True
    d = {'error':error}
    return render(request,'signupuser.html',d)

def recruiter(request):
    error = False
    if request.method == 'POST':
        u = request.POST['uname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        com = request.POST['company']
        con = request.POST['contact']
        gen = request.POST['gender']
        user = User.objects.create_user(email=e,username=u, password=p,last_name=l)
        sign = Recruiter.objects.create(user=user,mobile=con,image=i,company=com,gender=gen,type="recruiter",status='null')
        error = True
    d = {'error':error}
    return render(request, 'recruiter.html',d)
def admin_recruiter(request):
    error = False
    if request.method == 'POST':
        u = request.POST['uname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        com = request.POST['company']
        con = request.POST['contact']
        gen = request.POST['gender']
        user = User.objects.create_user(email=e,username=u, password=p,last_name=l)
        sign = Recruiter.objects.create(user=user,mobile=con,image=i,company=com,gender=gen,type="recruiter",status='null')
        error = True
    d = {'error':error}
    return render(request, 'admin_recruiter.html',d)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1=SignupUser.objects.get(user=user)
                if user1.type == "customer":
                    login(request, user)
                    error = "yes"
            except:
                error = "no"
        else:
            error = "not"
    d = {'error': error}
    return render(request,'login.html',d)


def Recruiter_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1=Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != "null":
                    login(request, user)
                    error = "yes"
                else:
                    error = "not"
            except:
                error = "no"
        else:
            error = "no"
    d = {'error': error}
    return render(request,'recruiter_login.html',d)

def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'loginadmin.html',d)
def Admin_home(request):
    course=0
    student=0
    student1=0
    student2=0
    sign = SignupUser.objects.all()
    instruct = Recruiter.objects.all()
    instruct1 = Add_job.objects.all()
    instruct2 = Apply.objects.all()
    for i in sign:
        course+=1
    for i in instruct:
        student+=1
    for i in instruct1:
        student1+=1
    for i in instruct2:
        student2+=1
    d ={'student':student,'course':course,'student1':student1,'student2':student2}
    return render(request,'admin_home.html',d)
def view_newrecruiter(request):
    data=Recruiter.objects.all()
    d={'data':data}
    return render(request,'view_newrecruiter.html',d)
def view_recruiter(request):
    data=Recruiter.objects.all()
    d={'data':data}
    return render(request,'view_recruiter.html',d)
def Assign_status(request,pid):
    submit = Recruiter.objects.get(id=pid)
    error = False
    if request.method=="POST":
        a = request.POST['status']
        submit.status = a
        submit.save()
        error = "yes"
    d = {'error':error,'data':submit}
    return render(request,'assign_status.html',d)
def delete_recruiter(request,pid):
    data=Recruiter.objects.get(id=pid)
    data.delete()
    return redirect('view_recruiter')
def delete_job(request,pid):
    data=Add_job.objects.get(id=pid)
    data.delete()
    return redirect('recruiter_viewjob')
def delete_user(request,pid):
    data=SignupUser.objects.get(id=pid)
    data.delete()
    return redirect('view_user')

def view_user(request):
    data=SignupUser.objects.all()
    d={'data':data}
    return render(request,'view_user.html',d)
def Admin_logout(request):
    logout(request)
    return redirect('home')
def recruiter_home(request):
    user=User.objects.get(id=request.user.id)
    data=Recruiter.objects.get(user=user)
    d ={'data':data}
    return render(request,'recruiter_home.html',d)


def Edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error = False
    user=User.objects.get(id=request.user.id)
    pro = Recruiter.objects.get(user=user)
    if request.method == 'POST':
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        m = request.POST['mobile']
        try:
            g = request.POST['gender']
            pro.gender=g
            pro.save()
        except:
            pass
        try:
            fi = request.FILES['image']
            pro.image = fi
            pro.save()
        except:
            pass
        pro.user.username=u
        pro.user.last_name=l
        pro.user.email=e
        pro.mobile=m
        pro.save()
        pro.user.save()
        error = True
    d = {'error':error,'pro':pro}
    return render(request, 'edit_profile.html',d)
def add_job(request):
    user=User.objects.get(id=request.user.id)
    data=Recruiter.objects.get(user=user)
    error = False
    if request.method == 'POST':
        c = request.POST['company']
        t = request.POST['title']
        s = request.POST['start_date']
        e = request.POST['end_date']
        de = request.POST['description']
        exp = request.POST['experience']
        p = request.POST['position']
        loc = request.POST['location']
        sk = request.POST['skills']
        i = request.FILES['image']
        data1=Recruiter.objects.get(company=c)
        Add_job.objects.create(recruiter=data1,title=t,start_date=s,end_date=e,description=de,experience=exp,location=loc,position=p,image=i,skills=sk)
        error = True
    d = {'error':error,'data':data}
    return render(request, 'add_job.html',d)
def recruiter_viewjob(request):
    user=User.objects.get(id=request.user.id)
    recruiter=Recruiter.objects.get(user=user)
    data=Add_job.objects.filter(recruiter=recruiter)
    d={'data':data}
    return render(request,'recruiter_viewjob.html',d)
def recruiter_logout(request):
    logout(request)
    return redirect('home')
def latest_job(request):
    data=Add_job.objects.all()
    d={'data':data}
    return render(request,'latest_job.html',d)
def user_home(request):
    user=User.objects.get(id=request.user.id)
    data=SignupUser.objects.get(user=user)
    d ={'data':data}
    return render(request,'home.html',d)


def UserEdit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error = False
    user=User.objects.get(id=request.user.id)
    pro = SignupUser.objects.get(user=user)
    if request.method == 'POST':
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        m = request.POST['mobile']
        try:
            g = request.POST['gender']
            pro.gender=g
            pro.save()
        except:
            pass
        try:
            fi = request.FILES['image']
            pro.image = fi
            pro.save()
        except:
            pass
        pro.user.username=u
        pro.user.last_name=l
        pro.user.email=e
        pro.mobile=m
        pro.save()
        pro.user.save()
        error = True
    d = {'error':error,'pro':pro}
    return render(request, 'useredit_profile.html',d)
def userlatest_job(request):
    data=Add_job.objects.all()
    user=User.objects.get(id=request.user.id)
    sign=SignupUser.objects.get(user=user)
    data1=Apply.objects.filter(sign=sign)
    li=[]
    for i in data1:
        li.append(i.job.id)
    d={'data':data,'li':li}
    return render(request,'userlatest_job.html',d)
def logout_user(request):
    logout(request)
    return redirect('home')
def job_detail(request,pid):
    data=Add_job.objects.get(id=pid)
    d={'data':data}
    return render(request,'job_detail.html',d)
def applyjob(request,pid):
    user=User.objects.get(id=request.user.id)
    data=SignupUser.objects.get(user=user)
    data1=Add_job.objects.get(id=pid)
    date1 = date.today()
    i3=data1.end_date.year
    i1=data1.end_date.day
    i2=data1.end_date.month
    n3=date1.year
    n1=date1.day
    n2=date1.month
    s3=data1.start_date.year
    s1=data1.start_date.day
    s2=data1.start_date.month
    error=""
    day1=i1+(i2*30)+(i3*365)
    day2=s1+(s2*30)+(s3*365)
    day3=n1+(n2*30)+(n3*365)
    if day3>day1:
        error="notable"
    elif day2>day3:
        error="close"
    else:
        if request.method == 'POST':
            i = request.FILES['image']
            Apply.objects.create(image=i,sign=data,job=data1)
            error="able"
    d={'error':error}
    return render(request,'apply.html',d)

def view_apply(request):
    user=User.objects.get(id=request.user.id)
    sign=Recruiter.objects.get(user=user)
    data=Apply.objects.all()
    li=[]
    for i in data:
        li.append(i.job.id)
    d={'data':data,'li':li,'sign':sign}
    return render(request,'view_apply.html',d)
def Change_Password(request):
    error = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'change_password.html',d)

def RecruiterChange_Password(request):
    error = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'change_password_instruct.html',d)
def Contact(request):
    return render(request,'contact.html')
def About(request):
    return render(request,'about.html')
def test_preparation(request):
    return render(request,'test preparation.html')   
def selection_process(request):
    return render(request,'selection_process.html')        
def user_form(request):
    return render(request,'user_form.html') 