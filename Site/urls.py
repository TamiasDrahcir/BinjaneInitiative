from django.urls import path
from . import views

urlpatterns = [
    path('home/eng=off',views.home,name="home"),
    path('home/eng=on', views.homeeng,name="homeeng"),
    path('about/eng=off',views.about,name="about"),
    path('about/eng=on', views.abouteng,name="abouteng"),
    path('service/eng=off',views.service,name="service"),
    path('service/eng=on', views.serviceeng,name="serviceeng"),
    path('contact/eng=off',views.contact,name="contact"),
    path('contact/eng=on',views.contacteng,name="contacteng"),
    path('team/eng=off',views.team,name="team"),
    path('team/eng=on',views.teameng,name="teameng"),
]