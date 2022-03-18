from email.headerregistry import Address
from pydoc import Doc
from django.shortcuts import render
from .models import Doctor_info
from patient.models import Patient_info
# Create your views here.

def dedit_record(request):
    return render (request,'doctor/dedit_record.html')

def dprediction(request):
    return render (request,'doctor/dprediction.html')

def dprofile(request):
    fname = Doctor_info.d_fname
    lname =Doctor_info.d_lname
    ssn=Doctor_info.d_ssn
    email=Doctor_info.d_email
    phone=Doctor_info.d_phone
    city=Doctor_info.d_city
    address=Doctor_info.d_address
    # photo=Doctor_info.d_photo
    return render (request,'doctor/dprofile.html',{
        "fname": fname ,
        "lname": lname,
        "ssn":ssn,
        "email":email,
        "phone":phone,
        "city":city,
        "address":address
    })

def drecord(request):
    return render (request,'doctor/drecord.html')    

def dpprofile(request):
    if request.method == "POST":
        dsearch=request.POST['dsearch'] 
        Patient_infos= Patient_info.objects.get(p_ssn = dsearch)
        return render (request,'doctor/dpprofile.html',{'dsearch':dsearch, 'Patient_info':Patient_infos})
    else:
      return render (request,'doctor/dpprofile.html',{})
        
    
    
    # fname = Patient_info.p_fname
    # lname =Patient_info.p_lname
    # ssn=Patient_info.p_ssn
    # email=Patient_info.p_email
    # phone=Patient_info.p_phone
    # city=Patient_info.p_city
    # hieght = Patient_info.p_height
    # wieght= Patient_info.p_weight
    # dtype=Patient_info.p_diatype
    # gender=Patient_info.p_gender
    # address=Patient_info.p_address
    # age=Patient_info.p_dateofbirth
    # photo=Doctor_info.d_photo
    # return render (request,'doctor/dpprofile.html',{
        # "fname": fname ,
        # "lname": lname,
        # "ssn":ssn,
        # "wieght":wieght,
        # "hieght": hieght,
        # "dtype": dtype,
        # "gender": gender,
        # "email":email,
        # "phone":phone,
        # "city":city,
        # "age":age,
        # "address":address


def dmedication_err(request):
    return render (request,'doctor/dmediction_err.html')   
# Create your views here.
