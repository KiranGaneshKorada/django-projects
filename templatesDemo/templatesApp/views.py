from django.shortcuts import render

# Create your views here.

def home(request):
     datadict={"name":"kiran"}
     return render(request,'templatesApp/index.html',context=datadict)
