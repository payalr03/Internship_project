from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Contact,Student,Attendance
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import io,csv
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    return render(request,'home.html')

def uploadcsv(request):
    template = "uploadcsv.html"  
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.warning(request,"This is not csv file,Please try again ")
        return redirect('/uploadcsv')
        return render(request,template)
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):        
        _, created = Student.objects.update_or_create(usn=column[0],name=column[1],email=column[2],attendance=column[3])               
    context = {}
    
    messages.info(request,"Your Record Has Been Uploaded and Updated")
    return redirect('/uploadcsv')   
    return render(request,'uploadfile.html',context)

def  attendance_download(request):
    items=Attendance.objects.all()
    response= HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="Student_Attendance.csv"'
    writer = csv.writer(response,delimiter=',')
    writer.writerow(['id','usn','name','email','branch','attend'])

    for obj in items:
        writer.writerow([obj.id,obj.usn,obj.name,obj.email,obj.branch,obj.attend])

    return response

def handleSignup(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        num=request.POST['num']
        gender=request.POST['gender']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1 != pass2:
            messages.warning(request,"PASSWORD DOESN'T MATCH, PLEASE TRY AGAIN")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request,"USERNAME EXISTS")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass2)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.warning(request,"REGISTRATION COMPLETE")
        return redirect('/login')
    return render(request,'signup.html')

def handleLogin(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/login") 
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.info(request,"LOGOUT SUCCESSFUL")
    return redirect('/login')

def about(request):
    return render(request,'about.html')

def attendance(request):
    if request.method == "POST":
        usn=request.POST['usn']
        name=request.POST['name']
        email=request.POST['email']
        branch=request.POST['branch']
        attend=request.POST['attend']
        query=Attendance(usn=usn,name=name,email=email,branch=branch,attend=attend)
        query.save()
        messages.info(request,"Record has been saved")
        return redirect('/')
    

    return render(request,'attendance.html')