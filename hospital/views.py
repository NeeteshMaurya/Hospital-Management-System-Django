from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0;
    p=0;
    a=0;
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    d1 = {'d':d,'p':p,'a':a}
    return render(request, 'index.html',d1)

def Login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
                return redirect('home')
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
        
    return render(request, 'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


#Doctor
def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d= {'doc':doc}
    return render(request, 'view_doctor.html', d)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=c,special=sp)
            error="no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_doctor.html',d)

def Update_Doctor(request, pid):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.filter(id=pid).update(name=n,mobile=c,special=sp)
            error="no"
        except:
            error = "yes"
    doc = Doctor.objects.get(id=pid)    
    d = {'doc':doc,'error':error}
    return render(request, 'update_doctor.html', d)


def Delete_Doctor(request, pid):   #pid is a variable
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')



#patient
def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d= {'pat':pat}
    return render(request, 'view_patient.html', d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        g = request.POST['gender']
        c = request.POST['contact']
        ad = request.POST['address']
        try:
            Patient.objects.create(name=n,gender=g,mobile=c,address=ad)
            error="no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_patient.html',d)

def Delete_Patient(request, pid):   #pid is a variable
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


#Appointment
def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d= {'appoint':appoint}
    return render(request, 'view_appointment.html', d)

def Bill(request):
    if not request.user.is_staff:
        return redirect('login')
    patient1 = Patient.objects.all()
    return render(request, 'bill.html', {'patient':patient1})

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doct = Doctor.objects.filter(name=d).first()
        patie = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doct,patient=patie,date1=d1,time1=t)
            error="no"
        except:
            error = "yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request, 'add_appointment.html',d)

def Delete_Appointment(request, pid):   #pid is a variable
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')