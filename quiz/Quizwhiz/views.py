from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from Quizwhiz.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def Quiz2(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        contact = Contact(name=name, email=email, city=city, date=datetime.today())
        
        try:
            contact.full_clean()  # Validate the model instance
            contact.save()
            return redirect('/Options2')
        except ValidationError as e:
            messages.error(request, "Error: " + str(e))
            return render(request, "Quiz2.html")
    
    return render(request, "Quiz2.html")

def Options2(request):
    messages.success(request, "Registration Successful !!")
    return render(request, "Options2.html")

def history(request):
    return render(request, "history.html")

def geography(request):
    return render(request, "geography.html")

def Phy(request):
    return render(request, "Phy.html")

def maths(request):
    return render(request, "maths.html")

