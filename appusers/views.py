from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth import login,logout
from  django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from .register import Userregister
# Create your views here.

def user_form(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=UserCreationForm()
    context={
        'form':form
    }
    return render(request,'appusers/register.html',context)

def login_view(request):

    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('../../works/form')
            
    else:
        form=AuthenticationForm()
    return render(request,'appusers/login.html',{'form':form})
def logout_view(request):
    logout(request)
    return redirect('../login/')