from django.urls import path, include
from . import views

urlpatterns = [
	path('artist-details/<int:pk>', views.ArtistDetailsView, name='artist_details'),
	path('', views.IndexView.as_view(), name='artists_home'),
]