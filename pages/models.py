# from email.policy import default
# from pyexpat import model
# from django.db import models
# from doctor.models import Doctor_info

# class Dlogin(models.Model):
#     d_ssn=models.OneToOneField(Doctor_info, on_delete=models.CASCADE)
#     d_password=models.CharField(max_length=50,blank=False)
    
    
#     def __str__(self):
#         return self.d_ssn    
#     class Meta :
#         verbose_name='doctor login'
#     class Meta:
#         ordering =['d_ssn']
    
    
    
# class Plogin(models.Model):
#     p_ssn=models.OneToOneField(Patient_info, on_delete=models.CASCADE)
#     p_password=models.CharField(default='xxxxxxx',max_length=50,blank=False)
    
    
#     def __str__(self):
#         return self.p_ssn    
    
    
#     class Meta :
#         verbose_name='patient login'
#     class Meta:
#         ordering =['p_ssn']