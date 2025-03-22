from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponse, redirect
import datetime
from home.models import *
from django.core.validators import EmailValidator, validate_email
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")
def about(request):
    return render(request,"Infrastructure.html")
def services(request):
    return HttpResponse("this is home page")
def contact(request):
    try: 
        
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            desc = request.POST.get("desc")
            cons = con(name=name, email=email, desc=desc)
            if [validate_email(email)]:
                cons.save()
                html = {'value': 1}
                return render(request, "contact.html", html)
    except :
        html = {'value': 0}
        return render(request, "contact.html", html)

    return render(request,"contact.html")
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        psw = request.POST.get("psw")
        if not reg.objects.filter(email=email,password = psw):
            html = {'value':1}
            return render(request,"login.html",html )
        else:
            person = {"name":reg.objects.filter(email=email)}
            return render(request,'user.html',person)
    return render(request,'login.html')
def register(request):
    try:
        if request.method == "POST":
            f_name = request.POST.get("fname")
            l_name = request.POST.get("lname")
            mail = request.POST.get("mail")
            psw = request.POST.get("psw")
            regist = reg(fname = f_name ,lname = l_name ,email=mail.lower(), password = psw,date  =datetime.datetime.today())
            if not reg.objects.filter(email=mail,password = psw):
                if [validate_email(mail)]:
                    regist.save()
                    return render(request,"login.html")
            else:
                return render(request,'register.html',{'value':1})
    except:
        html = {'value': 0}
        return render(request, "register.html", html)
    return render(request,'register.html')
def forgot(request):
    if request.method =="POST":
        email = request.POST.get("mail")
        if not reg.objects.filter(email=email ):
            html = {'value': 1}
            return render(request, "forgot.html", html)
        else:
            return render(request,'forgot1.html')
    return render(request,"forgot.html")

