from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def index(request):
    if not request.user.is_staff:
        return redirect('log_in')
    return render(request,'index.html')
    
def log_in(request):
    error=""
    if request.method == "POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        print(user)
        try:
            if user.is_authenticated:
                error="NO"
                login(request,user)
                print("user auth")
                return redirect('index')
                
            else:
                error="yes"    
        except:
            error="yes"
    d={'error':error}  
    print(d)
    return render(request,'log_in.html',d)   
       
def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('log_in')
def add_doctor(request):
    return render(request,'add_Doctor.html')
def remove_doctor(request):
    return render(request,'remove_Doctor.html')