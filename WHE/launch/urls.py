from django.urls import path, include
from . import views

urlpatterns = [
   path('aboutUs/', views.aboutUsView, name='launch_aboutUs'),
   path('contactUs/', views.contactUsView, name='launch_contactUs'),
   path('', views.homeview, name='launch_home'),
]