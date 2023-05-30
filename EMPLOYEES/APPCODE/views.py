from django.shortcuts import render, redirect
from .models import Employees
from django.contrib import messages

# Create your views here.
def index(request):
    data=Employees.objects.all()
    # print(data)
    # context={"data":data}
    # return render(request,"index.html",context)

    return render(request,"index.html", {"data":data})


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        position=request.POST.get('position')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        department=request.POST.get('department')
        salary=request.POST.get('salary')
        
        # print(name,email,position,age,gender,department,salary)
        query=Employees(name=name, email=email, position=position, age=age, gender=gender, department=department, salary=salary)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        position=request.POST['position']
        age=request.POST['age']
        gender=request.POST['gender']
        department=request.POST['department']
        salary=request.POST['salary']

        edit=Employees.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.position=position
        edit.age=age
        edit.gender=gender
        edit.department=department
        edit.salary=salary

        edit.save()
        messages.success(request, "Data Updated Successfully")
        return redirect("/")

    d=Employees.objects.get(id=id) 

    return render(request, "edit.html",{"d":d})


def deleteData(request,id):
    d=Employees.objects.get(id=id) 
    d.delete()
    messages.error(request, "Data deleted Successfully")
    return redirect("/")
