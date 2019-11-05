from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import datetime
from django.db.models import Q
from .models import Artist


class IndexView(generic.ListView):
    template_name = 'artists/artists_home.html'
    context_object_name = 'artist_list'

    def get_queryset(self):
        
        # self.starts = get_object_or_404(Event, name=self.kwargs['starts'])

        # return Event.objects.filter(starts=self.starts)
        return Artist.objects.all()


def ArtistDetailsView(request, pk):
    artist = get_object_or_404(Artist, id=pk)

    context = {
            'artist': artist
        }

    return render(request, 'artists/artists_description.html', context)