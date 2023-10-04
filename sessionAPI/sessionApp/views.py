from django.shortcuts import render,HttpResponse
from . import forms

# Create your views here.
def pageCount(request):
    count=request.session.get('count',0)
    count=count+1
    request.session['count']=count
    return render(request,'count.html',{'count':count})

def myCart(request):
    return render(request,'cart_items.html')

def addToCart(request):
    form=forms.CartItem()

    if request.method=='POST':
        form=forms.CartItem(request.POST)
        if form.is_valid():
            name=form.cleaned_data['itemName']
            quantity=form.cleaned_data['quantity']
            request.session[name]=quantity
            return myCart(request)

    return render(request,'add_to_cart.html',{'form':form})

def randomViewToHandleExceptionUsingMiddleWare(request):
    raise Exception("exception vachindi brooo")
    return HttpResponse("hiii i am handling exception using middleware")
