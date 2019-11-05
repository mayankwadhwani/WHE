from django.shortcuts import render
from django.views.generic import ListView

def homeview(request):
	return render(request, 'launch/home.html')

def contactUsView(request):
	return render(request, 'launch/contactUs.html')

def aboutUsView(request):
	return render(request, 'launch/aboutUs.html')
