from django.shortcuts import render

# Create your views here.

def homeProduct(request):
    return render(request,"productTemplates/index.html")

def electronicProducts(request):
    datadict={"heading":"Electronic","products":[{"name":"headphones","cost":"50k"},
                                                 {"name":"mblphone","cost":"500k"},
                                                 {"name":"laptop","cost":"100k"}]}
    return render(request,"productTemplates/products.html",context=datadict)
