from datetime import datetime
from django.db import models
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from numpy import choose
# from pages.models import Plogin
from zmq import NULL
from django.contrib.postgres.fields import ArrayField

class Patient_info (models.Model):
    # models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    p_ssn=models.CharField (max_length=50, unique= True ,blank=False)
    p_password = models.CharField (max_length=50,blank=False)
    type1='type1'
    type2='type2'
    male ='male'
    female ='female'
    gender_choices=[
        (male,'male'),
        (female,'female')
    ]
    diatype_choices=[
        
        (type1,'type1'),
        (type2,'type2')
    ]
    p_fname = models.CharField ( max_length=50,blank=False)
    p_lname = models.CharField(max_length=50,blank=False)
    p_email=models.EmailField( null=False)
    p_phone=models.CharField (max_length=50,blank=False)
    p_city=models.CharField(max_length=70)
    p_address= models.CharField(max_length=50)
    p_height= models.IntegerField(blank=False)
    p_weight=models.IntegerField(blank=False)
    p_age= models.IntegerField(blank=False)
    p_diatype=models.CharField (choices=diatype_choices,blank=True,null=True , max_length=20)
    p_gender=models.CharField (choices=gender_choices,blank=False , max_length=20)
    # class Record (models.Model):
    #     dyavalue=models.IntegerField(default='00',)
    
    
    def __str__ (self):
        return self.p_phone
    class Meta :
        verbose_name='patient personal data'
    class Meta:
        ordering =['p_ssn']

class M_record (models.Model):
    # p_ssn= models.ManyToOneRel()
    glucose= models.IntegerField(blank=False)
    blood_pressure= models.IntegerField(blank=False)
    insulin= models.IntegerField(blank=False)
    bmi= models.DecimalField(decimal_places=3,max_digits=3)
    
    
    
    
    
    
    
# class Rava (models.Patient_info):
#     dya = models.IntegerField()
    
# Create your models here.
