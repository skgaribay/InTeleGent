from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "login.html")

def about_view(request):
    return render(request, 'about.html')

def dashboard_view(request):
    return render(request, 'patient_dash.html')