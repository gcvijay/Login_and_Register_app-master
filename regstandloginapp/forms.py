from django import forms
class RegForm(forms.Form):
    Firstname = forms.CharField(max_length=10)
    Lastname = forms.CharField(max_length=10)
    Username = forms.CharField(max_length=10)
    PassWord = forms.CharField(max_length=10, widget=forms.PasswordInput())
    CpassWord = forms.CharField(max_length=10, widget=forms.PasswordInput())
    Mobilenumber = forms.CharField(max_length=10)
    Emailid = forms.EmailField()

class LoginForm(forms.Form):
    UserName = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput())
