from django.urls import path
from .views import *

app_name='core'
urlpatterns = [
    path('',home,name='home'),
    path('newsleter/',newsleter,name="newsleter"),
    path('contactus/',contactus,name='contact'),
]



