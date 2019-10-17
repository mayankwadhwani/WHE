from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.homeview, name='launch_home'),
   path('/contact', views.contactview, name = 'show_contact_page')
]