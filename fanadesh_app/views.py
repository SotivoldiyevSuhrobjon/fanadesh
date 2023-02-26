from django.shortcuts import render,redirect
from .models import *

def get_social_links():
    return SocialLink.objects.first()

def home(request):
    data = About.objects.all()
    admin= Admission.objects.all()
    why = WhyUs.objects.all()
    context = {
        'link': get_social_links(),
        'data': data,
        'admin': admin,
        'why': why,

    }
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        message=request.POST.get('message')
        contact = ContactUs.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message,
        )
        contact.save()
    return render(request, 'home.html',context)

def about(request):
    data = About.objects.all()
    context = {
        'link': get_social_links(),
        'data': data,

    }

    return render(request, 'about.html', context)

def admission(request):
    admin= Admission.objects.all()
    context={
        'link': get_social_links(),
        'admin': admin,
    }
    return render(request, 'admission.html', context)

def whyus(request):
    why = WhyUs.objects.all()
    context={
        'link': get_social_links(),
        'why': why,
    }
    return render(request, 'whyus.html', context)
    
def contactus(request):
    context={
        'link': get_social_links(),

    }
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        message=request.POST.get('message')
        contact = ContactUs.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message,
        )
        contact.save()
    return render(request, 'contactus.html', context)