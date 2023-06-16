from django.contrib import admin
from django.urls import path
from web import views
urlpatterns = [
    path('', views.index),
    path('quote',views.Get_Quote),

    path('service', views.services),
    
]
