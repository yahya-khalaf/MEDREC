from django.shortcuts import render
from django.http import HttpResponse

from patient.models import patient_info


def home(request):
    return render (request,'pages/home.html')

def register(request):
    return render (request,'pages/register.html')

def about(request):
    return render (request,'pages/about.html')


def login(request):
    return render (request,'pages/login.html')    




# Create your views here.
