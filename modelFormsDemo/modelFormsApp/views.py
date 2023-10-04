from django.shortcuts import render
from .forms import ProjectForm
from .models import Project

# Create your views here.

def index(request):
    return render(request,'modelFormsApp/index.html')


def projectsList(request):
    project_data=Project.objects.all()
    return render(request,'modelFormsApp/projectsList.html',{"project_list":project_data})

def addProject(request):
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid:
            form.save()
            return projectsList(request)
    return render(request,'modelFormsApp/addProject.html',{'form':form})


