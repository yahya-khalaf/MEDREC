from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models
from matplotlib.pyplot import cla
# from pages.models import Dlogin


class Doctor_info (models.Model):
    d_ssn=models.CharField (max_length=50,blank=False)
    d_password=models.CharField (max_length=50,blank=False)
    d_fname = models.CharField (max_length=50,blank=False)
    d_lname = models.CharField(max_length=50,blank=False)
    d_email=models.EmailField(default='medrecsite@bme.com', null=False)
    d_phone=models.CharField (max_length=50,blank=False)
    d_address=models.CharField(max_length=70,blank= True,null=True)
    d_city=models.CharField(max_length=70)
    d_photo= models.ImageField(upload_to='media/doctor', default='media/doctor/download.png')
    def __str__(self):
        return self.d_phone
    
    class Meta :
       verbose_name='doctor personal data'
    class Meta:
        ordering =['d_ssn']



# Create your models here.
