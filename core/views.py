from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def books(request):
    return render(request,'books.html')

def news(request):
    return render(request,'news.html')

def cars(request):
    return render(request,'cars.html')

def phones(request):
    return render(request,'phones.html')

def products(request):
    return render(request,'products.html')