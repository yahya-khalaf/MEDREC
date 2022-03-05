from email.policy import default
from pyexpat import model
from django.db import models


class dlogin(models.Model):
    d_ssn=models.CharField (max_length=50,blank=False, unique=True)
    d_password=models.CharField(max_length=50,blank=False)
    
    class Meta :
        verbose_name='doctor login'
    class Meta:
        ordering =['d_ssn']
    
    
    
class plogin(models.Model):
    p_ssn=models.CharField (max_length=50,blank=False, unique=True)
    p_password=models.CharField(max_length=50,blank=False)
    
    class Meta :
        verbose_name='patient login'
    class Meta:
        ordering =['p_ssn']