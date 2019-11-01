from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.db.models import Q
from .models import Event


class IndexView(generic.ListView):
    template_name = 'events/home.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        
        # self.starts = get_object_or_404(Event, name=self.kwargs['starts'])

        # return Event.objects.filter(starts=self.starts)
        return Event.objects.all()
