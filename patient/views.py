from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient_info
from .forms import Patient_infoForm
def patient (request):
    return render(request,'patient/patient.html')

def pedit_record(request):
    return render(request,'patient/pedit_record.html')


def pprediction(request):
    return render(request,'patient/pprediction.html')    


def pprofile(request):
    # id= Patient_info.objects.all(ssn='12345678')
    fname = Patient_info.p_fname
    lname =Patient_info.p_lname
    ssn=Patient_info.p_ssn
    password=Patient_info.p_password
    email=Patient_info.p_email
    phone=Patient_info.p_phone
    city=Patient_info.p_city
    hieght = Patient_info.p_height
    wieght= Patient_info.p_weight
    dtype=Patient_info.p_diatype
    gender=Patient_info.p_gender
    address=Patient_info.p_address
    age=Patient_info.p_age
    # photo=Doctor_info.d_photo
    return render(request,'patient/pprofile.html',{
        
        "fname": fname,
        "lname": lname,
        "ssn":ssn,
        "password":password,
        "wieght":wieght,
        "hieght": hieght,
        "dtype": dtype,
        "gender": gender,
        "email":email,
        "phone":phone,
        "city":city,
        "age":age,
        "address":address
        
    })

    


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
