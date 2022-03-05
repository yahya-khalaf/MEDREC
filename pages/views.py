from django.shortcuts import render
from django.http import HttpResponse

from patient.models import patient_info


def home(request):
    return render (request,'pages/home.html')

def dlogin(request):
    return render (request,'pages/dlogin.html')

def phome(request):
    return render (request,'pages/phome.html')


def plogin(request):
    return render (request,'pages/plogin.html')    



def signup(request):
    return render (request,'pages/signup.html')    


# Create your views here.
