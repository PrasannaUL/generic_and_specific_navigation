

from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('sahana/',sahana,name='sahana'),
    path('sruthi/',sruthi,name='sruthi')
]