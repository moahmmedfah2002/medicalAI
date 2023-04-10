from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.current_datetime,name="current_datetime"),

    path('recherche', views.recherche, name='recherche'),
]