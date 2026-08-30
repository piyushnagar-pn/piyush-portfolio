from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def skill(request):
    return render(request, "skill.html")  

def contact(request):
    return render(request, "contact.html")


