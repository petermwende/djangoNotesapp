from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate signin, signout

def EnterData(request):
    if request.method="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        #print(name,email,age)
        return redirect("/")
    return render(request,"index.html")

def UpdateData(request,id):
    if request.method="POST":
        name= request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        edit.name=name
        edit.email=email
        edit.age=age
        edit.save()
        return redirect("/")

    return render(request,"")
