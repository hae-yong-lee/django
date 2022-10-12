from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pybo/', views.pybo),
    path('read/<id>/', views.read),
]