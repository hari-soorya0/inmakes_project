from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
]