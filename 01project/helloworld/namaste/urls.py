from django.urls import path
from . import homepage

urlpatterns = [
    path('', views.homepage, name='home'),
]
