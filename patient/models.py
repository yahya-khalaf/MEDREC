from datetime import datetime
from django.db import models
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from numpy import choose
from pages.models import plogin
from zmq import NULL
from django.contrib.postgres.fields import ArrayField

class patient_info (models.Model):
    
    p_ssn=models.OneToOneField(plogin, on_delete=models.CASCADE)
    
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
    
    p_fname = models.CharField (max_length=50,blank=False)
    p_lname = models.CharField(max_length=50,blank=False)
    p_ssn=models.CharField (max_length=50,blank=False, unique=True)
    p_email=models.EmailField(default='medrecsite@bme.com' , null=False)
    p_phone=models.CharField (max_length=50,blank=False)
    p_city=models.CharField(max_length=70)
    p_address= models.CharField(max_length=50)
    p_height= models.IntegerField(blank=False)
    p_weight=models.IntegerField(blank=False)
    p_dateofbirth= models.DateField (blank=False)
    p_diatype=models.CharField (choices=diatype_choices,blank=True,null=True , max_length=20)
    p_gender=models.CharField (choices=gender_choices,blank=False , max_length=20)
    def __str__ (self):
        return self.ssn
    class Meta :
        verbose_name='patient personal data'
    class Meta:
        ordering =['p_ssn']






class patientRecord (models.Model):
    p_ssn=models.OneToOneField(plogin, on_delete=models.CASCADE)
    glucose = ArrayField(ArrayField(models.IntegerField()))
    
    # data = models.ForeignKey(readings, on_delete=models.CASCADE)

    def __str__ (self):
        return self.ssn
    class Meta :
        verbose_name='patient history data'
    class Meta:
        ordering =['p_ssn']





# Create your models here.
