from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor,Patient,Appointment
# Create your views here.
def home(request):
    if not request.user.is_staff:
        logout(request)
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
    if not request.user.is_staff:
        return redirect('log_in')
    if request.method == "POST":
        n=request.POST['Name']
        m=request.POST['mobile']
        s=request.POST['special']
        doctor=Doctor(Name=n,mobile=m,special=s)
        doctor.save()
        return redirect('view_doctor')
    return render(request,'add_Doctor.html')
def remove_doctor(request,id=None):
    if not request.user.is_staff:
        return redirect('log_in')
    if id is not None:
        pk=id
        doctor=Doctor.objects.get(id=pk)
        doctor.delete()
        return redirect('view_doctor')
def view_doctor(request):
    if not request.user.is_staff:
        return redirect('log_in')
    doc=Doctor.objects.all()
    return render(request,'view_doctor.html',{'doc':doc})
def add_patient(request):
    if not request.user.is_staff:
        return redirect('log_in')
    if request.method == "POST":
        n=request.POST['name']
        g=request.POST['gender']
        m=request.POST['mobile']
        a=request.POST['address']
        patient=Patient(name=n,gender=g,mobile=m,address=a)
        patient.save()
        return redirect('view_patient')
    return render(request,'add_patient.html')
def remove_patient(request,id=None):
    if not request.user.is_staff:
        return redirect('log_in')
    if id is not None:
        pk=id
        patient=Patient.objects.get(id=pk)
        patient.delete()
        return redirect('view_patient')
def view_patient(request):
    if not request.user.is_staff:
        return redirect('log_in')
    doc=Patient.objects.all()
    return render(request,'view_patient.html',{'doc':doc})
   