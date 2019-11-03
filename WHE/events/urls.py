from django.urls import path, include
from . import views

urlpatterns = [
	path('cal/<int:year>/<int:month>', views.Cal, name='events_calendar'),
	path('', views.IndexView.as_view(), name='events_home'),
]