from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import *                       # importing from models

# Create your views here.

def index(request):
    if request.method == "POST":
        usn = request.POST.get('usn', '')
        name = request.POST.get('name', '')
        sem = request.POST.get('sem', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        if usn and name and sem and phone and email:
            contact = Contact(usn = usn, name = name, sem = sem, phone = phone, email = email)
            contact.save()
        else:
            return HttpResponse("<h1>Enter full details.</h1>")

    return render(request, 'index.html')