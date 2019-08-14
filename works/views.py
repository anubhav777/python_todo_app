from django.shortcuts import render,redirect
from django.http import request
from .models import Todowoorks
from .forms import Todo_Forms
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/appusers/login/')
def Form_display(request):
    if request.method == 'POST':
        form=Todo_Forms(request.POST or None,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.userid=request.user
            print(request.user)
            instance.save()
            form=Todo_Forms()
    else:
        
        form=Todo_Forms()
    userid=request.user
    print(userid)
    obj=Todowoorks.objects.filter(userid=userid)
    context={
            'form':form,
             'obj':obj
        }
    return render(request,'work/todoform.html',context)

def edit_form(request,id):
    obj=Todowoorks.objects.get(id=id)
    form=Todo_Forms(request.POST or None,instance=obj)
    if form.is_valid():
        form.workname=form.cleaned_data['workname']
        print(form.cleaned_data['workname'])
        form.save()
        return redirect('../form')
    
    return render(request,'work/editform.html',{'obj':obj,'form':form})



def form_delete(request,id):
    obj=Todowoorks.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
    return redirect('../form')