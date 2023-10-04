from django.shortcuts import render,HttpResponse
from django.views.generic import View

# Create your views here.

class GreetingsView(View):
    greetingMsg='hii ra jaffa'
    def get(self,request):
        return HttpResponse(self.greetingMsg)

