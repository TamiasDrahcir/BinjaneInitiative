from django.urls import path
from . import views

urlpatterns = [
    path('home/eng=off',views.home,name="home"),
    path('home/eng=on', views.homeeng,name="homeeng"),
    path('about/eng=off',views.about,name="about"),
    path('about/eng=on', views.abouteng,name="abouteng"),
    path('service/eng=off',views.service,name="service"),
    path('service/eng=on', views.serviceeng,name="serviceeng"),
    path('submit_service/eng=off',views.servicesub,name="servicesub"),
    path('submit_service/eng=on',views.servicesubeng,name="servicesubeng"),
    path('contact/eng=off',views.contact,name="contact"),
    path('contact/eng=on',views.contacteng,name="contacteng"),
    path('submit_contact/eng=off',views.contactsub,name="contactsub"),
    path('submit_contact/eng=on',views.contactsubeng,name="contactsubeng"),
    path('team/eng=off',views.team,name="team"),
    path('team/eng=on',views.teameng,name="teameng"),
    path('kaleidoscope/eng=off',views.kaleidoscope,name="kaleidoscope"),
    path('submit_kaleidoscope/eng=off',views.kaleidoscopesub,name="kaleidoscopesub"),
    path('kaleidoscope/eng=on',views.kaleidoscopeeng,name="kaleidoscopeeng"),
    path('submit_kaleidoscope/eng=on',views.kaleidoscopesub,name="kaleidoscopesubeng"),
    path('tajian/eng=off',views.tajian,name="tajian"),
    path('submit_tajian/eng=off',views.tajiansub,name="tajiansub"),
    path('tajian/eng=on',views.tajian,name="tajiansub"),
    path('submit_tajian/eng=on',views.tajiansubeng,name="tajiansubeng"),
]