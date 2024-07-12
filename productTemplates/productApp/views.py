from django.shortcuts import render

# Create your views here.

def electronics(request):
    product_dist={
        "heading": "electronics",
        "product1":"MAC",
        "product2":"Iphone",
        "product3":"Dell"
    }
    return render(request,'productApp/products.html',product_dist)

def toys(request):
    product_dist={
        "heading": "electronics",
        "product1":"Car",
        "product2":"Drone",
        "product3":"Rocket Launcher"
    }
    return render(request,'productApp/products.html',product_dist)

def shoes(request):
    product_dist={
        "heading": "electronics",
        "product1":"Nike",
        "product2":"Adidas",
        "product3":"Reebok"
    }
    return render(request,'productApp/products.html',product_dist)

def index(request):
    return render(request,'productApp/index.html')

def new(request):
    return render(request,)