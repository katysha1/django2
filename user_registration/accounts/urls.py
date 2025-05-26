from tkinter.font import names

from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('register/', views.register, name = 'register'),
    # path('', views.index1, name= 'index1'),
]