from django.urls import path
from . import views

urlpatterns = [
    path('home/eng=off',views.home,name="home"),
    path('home/eng=on', views.homeeng,name="homeeng"),
    path('about/eng=off',views.about,name="about"),
    path('service/eng=off',views.service,name="service"),
    path('contact/eng=off',views.contact,name="contact")
]