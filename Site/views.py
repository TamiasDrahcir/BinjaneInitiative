from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'Site/home.html')

def homeeng(request):
    return render(request,'Site/homeeng.html')

def about(request):
    return render(request,'Site/about.html')

def abouteng(request):
    return render(request,'Site/abouteng.html')

def service(request):
    return render(request,'Site/service.html')

def serviceeng(request):
    return render(request,'Site/serviceeng.html')

def contact(request):
    return render(request,'Site/contact.html')

def contacteng(request):
    return render(request,'Site/contacteng.html')

def team(request):
    return render(request,'Site/team.html')

def teameng(request):
    return render(request,'Site/teameng.html')