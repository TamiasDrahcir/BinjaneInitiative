from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import *

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

def servicesub(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        interest = request.POST.get('interest', '')
        
        # Format the email message with all fields
        email_message = f"""
志愿者表回复

姓名: {name}
电子邮件: {email}
电话: {phone}
兴趣: {interest}
        """
        
        try:
            send_mail(
                subject=f'来自{name}的志愿者表回复',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Debug print
            context['error'] = str(e)
            
        # Store all form data in context
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'interest': interest,
        })

    return render(request,'Site/servicesub.html',context)

def servicesubeng(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        interest = request.POST.get('interest', '')
        
        # Format the email message with all fields
        email_message = f"""
Volunteer Form Response

Name: {name}
Email: {email}
Phone: {phone}
Interest: {interest}
        """
        
        try:
            send_mail(
                subject=f'Volunteer Form Response from {name}',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Debug print
            context['error'] = str(e)
            
        # Store all form data in context
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'interest': interest,
        })

    return render(request,'Site/servicesubeng.html',context)

def contact(request):
    return render(request,'Site/contact.html')

def contacteng(request):
    return render(request,'Site/contacteng.html')

def contactsub(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # Format the email message with all fields
        email_message = f"""
联系表回复

姓名: {name}
电子邮件: {email}
电话: {phone}
主题: {subject}

消息如下:
{message}
        """
        
        try:
            send_mail(
                subject=f'来自{name}的联系表回复',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Debug print
            context['error'] = str(e)
            
        # Store all form data in context
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,
        })
    
    return render(request, 'Site/contactsub.html', context)

def contactsubeng(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # Format the email message with all fields
        email_message = f"""
Contact Form Response

Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}
        """
        
        try:
            send_mail(
                subject=f'Contact Form Response from {name}',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Debug print
            context['error'] = str(e)
            
        # Store all form data in context
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,
        })
    
    return render(request, 'Site/contactsubeng.html', context)

def team(request):
    profiles = profile.objects.all()
    dictionary = {
        'profiles': profiles,
    }
    return render(request,'Site/team.html',dictionary)

def teameng(request):
    profiles = profile.objects.all()
    dictionary = {
        'profiles': profiles,
    }
    return render(request,'Site/teameng.html',dictionary)

def kaleidoscope(request):
    gallery = category.objects.filter(english_name='Human Kaleidoscope').first()
    dictionary = {
        'gallery': gallery,
        'name': gallery.chinese_name,
        'description': gallery.chinese_description,
        'history': gallery.gallery_set.filter(category_id=gallery.id).all(),
    }
    return render(request,'Site/kaleidoscope.html',dictionary)

def kaleidoscopeeng(request):
    return render(request,'Site/kaleidoscopeeng.html')

def kaleidoscopesub(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        interest = request.POST.get('interest', '')
        
        # Format the email message with all fields
        email_message = f"""
投稿表回复

姓名: {name}
电子邮件: {email}
电话: {phone}
感兴趣的领域: {interest}
        """

        try:
            send_mail(
                subject=f'来自{name}的人间万花筒表回复',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Debug print
            context['error'] = str(e)

        # Store all form data in context
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'interest': interest,
        })

    return render(request, 'Site/kaleidoscopesub.html', context)

def kaleidoscopesubeng(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        interest = request.POST.get('interest', '')
        
        # Format the email message with all fields
        email_message = f"""
kaleidoscope Submission Form Response
Name: {name}
Email: {email}
Phone: {phone}
Interest: {interest}
        """

        try:
            send_mail(
                subject=f'Gallery Submission Form Response from {name}',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")


def tajian(request):
    gallery = category.objects.filter(english_name='Tajian').first()
    dictionary = {
        'gallery': gallery,
        'name': gallery.chinese_name,
        'description': gallery.chinese_description,
        'history': gallery.gallery_set.filter(category_id=gallery.id).all(),
    }
    return render(request,'Site/tajian.html',dictionary)

def tajianeng(request):
    return render(request,'Site/tajianeng.html')

def tajiansub(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        interest = request.POST.get('interest', '')
        
        # Format the email message with all fields
        email_message = f"""
投稿表回复

姓名: {name}
电子邮件: {email}
电话: {phone}
感兴趣的领域: {interest}
        """

        try:
            send_mail(
                subject=f'来自{name}的投稿表回复',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Debug print
            context['error'] = str(e)

        # Store all form data in context
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'interest': interest,
        })

    return render(request, 'Site/tajiansub.html', context)

def tajiansubeng(request):
    context = {}
    if request.method == "POST":
        
        # Get all form fields
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        interest = request.POST.get('interest', '')
        
        # Format the email message with all fields
        email_message = f"""
Gallery Submission Form Response
Name: {name}
Email: {email}
Phone: {phone}
Interest: {interest}
        """

        try:
            send_mail(
                subject=f'Gallery Submission Form Response from {name}',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email sent successfully")  # Debug print
            context['success'] = True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
                # Store all form data in context
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'interest': interest,
        })

    return render(request, 'Site/tajiansub.html', context)