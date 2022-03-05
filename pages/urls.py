from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home' ),
    path('phome', views.phome, name ='phome' ),
    path('dlogin', views.dlogin, name ='dlogin' ),
    path('plogin', views.plogin, name ='plogin' ),
    path('signup', views.signup, name ='signup' )
    ] 