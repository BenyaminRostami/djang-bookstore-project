from django.urls import path
from .views import *
urlpatterns = [
   path('' , Home_Page_Views.as_view() , name= 'home')
]
