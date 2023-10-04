from django.shortcuts import render
from .models import Employee,Programmer,Project

# Create your views here.

def empData(request):
    empRawData=Employee.objects.all()
    progRawData=Programmer.objects.all()
    projRawData=Project.objects.all()
    Dict={"employes":empRawData,"programmers":progRawData,"projects":projRawData}
    print(Dict['projects'])
    return render(request,'empApp/displayEmpData.html',context=Dict)


