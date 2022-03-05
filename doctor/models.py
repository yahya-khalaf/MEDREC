from django.db import models
from matplotlib.pyplot import cla
from pages.models import dlogin


class doctor_info (models.Model):
    d_ssn=models.OneToOneField(dlogin, on_delete=models.CASCADE)
    
    d_fname = models.CharField (max_length=50,blank=False)
    d_lname = models.CharField(max_length=50,blank=False)
    d_ssn=models.CharField (max_length=50,blank=False, unique=True)
    d_email=models.EmailField(default='medrecsite@bme.com', null=False)
    d_phone=models.CharField (max_length=50,blank=False)
    d_city=models.CharField(max_length=70)


    class Meta :
       verbose_name='doctor personal data'
    class Meta:
        ordering =['d_ssn']



# Create your models here.
