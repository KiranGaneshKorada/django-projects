from django.shortcuts import render,HttpResponse
from . import forms

# Create your views here.

def home(request):
    # setting a cookie to browser
    request.session.set_test_cookie()
    return HttpResponse("testing cookie")

def page2(request):
    # this returns boolean wheather browser is sending back cookie(data) or not 
    if request.session.test_cookie_worked():
        print("browser is sending data")
        request.session.delete_test_cookie()
    return HttpResponse("page 2 receiving cookie data and  deleting data")

def countView(request):
    if 'count' in request.COOKIES:
        count=int(request.COOKIES['count'])+1
    else:
        count=1
    response=render(request,'count.html',{'count':count})
    response.set_cookie('count',count)
    return response

def cartList(request):
    return render(request,'cart_items.html')

def addToCart(request):
    form=forms.CartItem()
    response=render(request,'add_to_cart.html',{'form':form})

    if request.method=='POST':
        form=forms.CartItem(request.POST)
        if form.is_valid() :
            name=form.cleaned_data['itemName']
            quantity=form.cleaned_data['quantity']
            request.COOKIES['form']={name:quantity}
            print(request.COOKIES)
            #return cartList(request) returning to another view doesnt add data to cookies
    else:
        response.set_cookie('form',{})
        print(request.COOKIES)
    return response




