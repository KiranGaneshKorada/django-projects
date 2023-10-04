from django.shortcuts import render,HttpResponse

# Create your views here.

def displayQuote(request):
    return HttpResponse("<h1>consistency beats talent in a long run</h1>")
