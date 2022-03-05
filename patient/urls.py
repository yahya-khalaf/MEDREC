from django.urls import path
from . import views


urlpatterns = [
    path ('register',views.register,name='register')
    # path('', views.profile, name ='profile' ),
    # path('history', views.history, name ='history' ),
    # path('prediction', views.prediction, name ='prediction' ),
    # path('data', views.data, name ='data' ),


    ] 