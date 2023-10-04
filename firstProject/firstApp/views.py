from django.shortcuts import render,HttpResponse

# Create your views here.

def display(request):
    return HttpResponse("<h1>this is my first django application</h1>")
