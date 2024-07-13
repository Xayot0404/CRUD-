from django.shortcuts import render,redirect
from .form import *
from .models import *
from django.contrib.auth.decorators import login_required 
from django.urls import is_valid_path
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


@login_required()
def editView(request,eddid):
    editcreds=CRUDmodel.objects.get(id=eddid)
    if request.method=="POST":
        form = CRUDform(request.POST,instance=editcreds)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return('show.html')
    form = CRUDform(instance=editcreds)
    projectFilter = CRUDmodel.objects.filter(id=eddid)
    ctx={
        'form':form,
        "projectFilter": projectFilter
        
    }
    return render(request,'edit.html',ctx)
            
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
    
