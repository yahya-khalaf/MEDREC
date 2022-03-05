from django.urls import path
from . import views


urlpatterns = [
    path ('patient',views.patient,name='patient'),
    path('pedit_record', views.pedit_record, name ='pedit_record' ),
    path('pprediction', views.pprediction, name ='pprediction' ),
    path('pprofile', views.pprofile, name ='pprofile' ),
    path('precord', views.precord, name ='precord' ),


    ] 