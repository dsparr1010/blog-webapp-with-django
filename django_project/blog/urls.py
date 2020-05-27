from django.urls import path
from . import views

urlpatterns = [
    #views.home is a function
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
