from cProfile import label
from attr import fields
from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from .models import Patient_info,M_record
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class M_record ():
    



class Patient_infoForm (UserCreationForm): 
    first_name = forms.CharField ( max_length=50,widget=forms.TextInput(attrs= {'size':'50','class':'special'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs= {'size':'50','class':'form-control'}))
    email=forms.EmailField( widget=forms.EmailInput(attrs= {'size':'50','class':'form-control'}))
    phone_number=forms.CharField (max_length=50,widget=forms.NumberInput(attrs= {'size':'50','class':'form-control'}))
    city=forms.CharField(max_length=70,widget=forms.TextInput(attrs= {'size':'50','class':'form-control'}))
    address= forms.CharField(max_length=50,widget=forms.TextInput(attrs= {'size':'50',  'class':'form-control'}))
    height= forms.IntegerField(widget=forms.NumberInput(attrs= {'class':'form-control','size':'50'}))
    weight=forms.IntegerField(widget=forms.NumberInput(attrs= {'class':'form-control','size':'50'}))
    age= forms.IntegerField(widget=forms.NumberInput(attrs= {'class':'form-control','size':'50'}))
    diabetes_type=forms.CharField (max_length=50,widget=forms.TextInput(attrs= {'class':'form-control','size':'50'}))
    gender=forms.CharField (max_length=50,widget=forms.TextInput(attrs= {'class':'form-control','size':'50'}))
    
    # Patient_infoForm.widget.attrs.update(size='40')
    class Meta:
        model = User
        fields= ('first_name','last_name' ,'username','email','phone_number','city','address','height','weight','age','diabetes_type','gender')
    def __init__(self, *args, **kwargs):
        super(Patient_infoForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['size']='50'
        self.fields['password1'].widget.attrs['size']='50'
        self.fields['password2'].widget.attrs['size']='50'
        
# creat patient personal data form

# class Patient_infoForm (ModelForm): 
#     class Meta:
#         model = Patient_info
#         fields = ('__all__')
#         labels = {
#             'p_ssn':'ssn',
#             'p_password':'password',
#             'p_fname':'first name',
#             'p_lname':'last name',
#             'p_email':'email address',
#             'p_phone':'phone number',
#             'p_city':'city',
#             'p_address':'address',
#             'p_height':'hieght' ,
#             'p_weight':'wieght',
#             'p_age':'age',
#             'p_diatype':'diabetes type',
#             'p_gender':'gender',     
            
#         }
#         widgets ={
                        
#             'p_ssn':forms.TextInput(attrs= {'class':'form-control' , 'placeholder':'Enter your social security number'}),
#             'p_password' : forms.PasswordInput(attrs= {'class':'form-control' , 'placeholder':'Enter your password'}),
#             'p_fname':forms.TextInput(attrs= {'class':'form-control' , 'placeholder':'first name'}),
#             'p_lname': forms.TextInput(attrs= {'class':'form-control' , 'placeholder':'last name'}),
#             'p_email':forms.EmailInput(attrs= {'class':'form-control' , 'placeholder':'email'}),
#             'p_phone':forms.NumberInput(attrs= {'class':'form-control' , 'placeholder':'phone number'}),
#             'p_city':forms.TextInput(attrs= {'class':'form-control' ,'placeholder':'your city'}),
#             'p_address': forms.TextInput(attrs= {'class':'form-control' , 'placeholder':'home address'}),
#             'p_height': forms.NumberInput(attrs= {'class':'form-control' ,'placeholder':'hight in cm'}),
#             'p_weight':forms.NumberInput(attrs= {'class':'form-control' , 'placeholder':'wieght in kg'}),
#             'p_age': forms.NumberInput(attrs= {'class':'form-control' ,'placeholder':'age'}),
#             # 'p_diatype':forms.TextInput(attrs= {'class':'form-control' ,'type': 'text', 'placeholder':'choose diabetes type'}),
#             # 'p_gender':forms.TextInput(attrs= {'class':'form-control' ,'type': 'text', 'placeholder':'gender'})
            
            
            
            
#             }