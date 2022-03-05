from django.contrib import admin

from patient.models import patient_info
from patient.models import patientRecord

# from .models import patientID
# Register your models fhere.

# admin.site.register(patientID)
admin.site.register(patient_info)
admin.site.register(patientRecord)

# admin.site.register('register')
