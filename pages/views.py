from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "login.html")

def about_view(request):
    return render(request, "about.html")

def dashboard_view(request):
    return render(request, "patient_dash.html")

def recs_view(request):
    return render(request, "patient_recs.html")

def chat_view(request):
    return render(request, "patient_chat.html")

def book_view(request):
    return render(request, "book.html")

def appointments_view(request):
    return render(request, "patient_calendar.html")