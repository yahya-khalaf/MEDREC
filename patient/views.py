from django.shortcuts import render
from django.http import HttpResponse

from patient.models import patient_info


def patient (request):
    return render(request,'patient/patient.html')

def pedit_record(request):
    return render(request,'patient/pedit_record.html')


def pprediction(request):
    return render(request,'patient/pprediction.html')    


def pprofile(request):
    return render(request,'patient/pprofile.html')


def precord(request):
    return render(request,'patient/precord.html')



# def register(request):
#     fname= request.POST.get('first_name')
#     lname= request.POST.get('last_name')
#     ssn= request.POST.get('SSN')
#     password= request.POST.get('password')
#     email= request.POST.get('email')
#     phone= request.POST.get('phone')
#     city= request.POST.get('city')
#     address= request.POST.get('address')
#     height= request.POST.get('height')
#     weight= request.POST.get('weigh')
#     age= request.POST.get('Age')
#     diatype= request.POST.get('Diabetestype')
#     gender= request.POST.get('gender')
   
   
#     data = patient_info (fname=fname,lname=lname,ssn=ssn,
#     password=password,email=email,phone=phone,city=city,
#     address=address,height=height,weight=weight,age=age,
#     diatype=diatype,gender=gender)
#     data.save()

#     return render(request,'register.html')

# # Create your views here.



# # Create your views here.
