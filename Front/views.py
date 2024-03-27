from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def services(request):
    return render(request,"services.html")

def apropos(request):
    return render(request,"apropos.html")

def recrutement(request):
    return render(request,"recrutement.html")

def contact(request):
    return render(request,"contact.html")
