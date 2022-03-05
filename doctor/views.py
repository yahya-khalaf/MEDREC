from django.shortcuts import render

# Create your views here.

def dedit_record(request):
    return render (request,'doctor/dedit_record.html')

def dprediction(request):
    return render (request,'doctor/dprediction.html')

def dprofile(request):
    return render (request,'doctor/dprofile.html')


def drecord(request):
    return render (request,'doctor/drecord.html')    

def dpprofile(request):
    return render (request,'doctor/dpprofile.html')   


def dmedication_err(request):
    return render (request,'doctor/dmediction_err.html')   
# Create your views here.
