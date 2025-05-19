from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'Site/home.html')

def homeeng(request):
    return render(request,'Site/homeeng.html')

def about(request):
    return render(request,'Site/about.html')

def service(request):
    return render(request,'Site/service.html')

def contact(request):
    return render(request,'Site/contact.html')