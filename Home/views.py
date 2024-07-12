from django.shortcuts import render,redirect
from .form import *
from .models import *


def CrudView(request):
    if request.method == 'POST':
        form = CRUDform(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/show')
        else:
            form=CRUDform()
    ctx ={
            'CRUDform':CRUDform   
        }
    return render(request,'index.html',ctx)

def show(request):
     cruds = CRUDmodel.objects.all()
     return render(request,'show.html',{'cruds':cruds})

def edit(request,id):
    creds=CRUDmodel.objects.get(id=id)
    return render(request,'edit.html',{'creds':creds})
            
def update(request,id):
    creds=CRUDmodel.objects.get(id=id)
    form=CRUDform(request.POST,instance=creds)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'creds':creds})

def delete(request,id):
    creds=CRUDmodel.objects.get(id=id)
    creds.delete()
    return redirect('/show')
    
