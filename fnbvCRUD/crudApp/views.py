from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

# this login decorator allows the views to render only if user is logged in otherwise it redirects to login page

# Create your views here.
@login_required
def studentsList(request):
    students_data=Student.objects.all()
    return render(request,'crudApp/studentsList.html',context={"students_data":students_data})

@login_required
def createStudent(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return studentsList(request)
    return render(request,'crudApp/createStudent.html',{"form":form})

@login_required
def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return studentsList(request)

"""
# brute force approach in updateStudent.html also form is created manually
def updateStudent(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return studentsList(request)
    return render(request,'crudApp/updateStudent.html',{'student':student})

"""

@login_required
# fast approach
def updateStudent(request,id):
    student=Student.objects.get(id=id)
    # here form will be populated by student data 
    data_form=StudentForm(instance=student)
    if request.method=='POST':
        # here post data will jump on student instance and replace the change and return a form
        data_form=StudentForm(request.POST,instance=student)
        if data_form.is_valid():
            data_form.save()
            return studentsList(request)
    return render(request,'crudApp/updateStudent.html',{'data_form':data_form})
