from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg
from .forms import RegForm,LoginForm

class Home(View):
    def get(self,request):
        return render(request,template_name='home.html')

class Reginput(View):
    def get(self,request):
        con_dict={"regform" : RegForm() }
        return render(request,template_name='reginput.html',context=con_dict)

class Logininput(View):
    def get(self,request):
        con_dict={"Loginfrom" : LoginForm() }
        return render(request,template_name='logininput.html',context=con_dict)

class Register(View):
    def post(self,request):
        rf=RegForm(request.POST)
        if rf.is_valid():
            r1=Reg(FirstName=rf.cleaned_data['Firstname'],
                    LastName=rf.cleaned_data['Lastname'],
                    UserName=rf.cleaned_data['Username'],
                    Password=rf.cleaned_data['PassWord'],
                    Cpassword=rf.cleaned_data['CpassWord'],
                    MobileNumber=rf.cleaned_data['Mobilenumber'],
                    EmailId=rf.cleaned_data['Emailid'])
            r1.save()
            return HttpResponse("Registration successful")

class Login(View):
    def post(self,request):
        lf=LoginForm(request.POST)
        if lf.is_valid():
            uname1=lf.cleaned_data['UserName']
            password1=lf.cleaned_data['Password']
            res=Reg(UserName=uname1,Password=password1)
            if res:
                return HttpResponse("Login successful")
            else:
                return HttpResponse("Login Failed")

