from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.db.models import Q
from .models import Event
import calendar


class IndexView(generic.ListView):
    template_name = 'events/home.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        
        # self.starts = get_object_or_404(Event, name=self.kwargs['starts'])

        # return Event.objects.filter(starts=self.starts)
        return Event.objects.all()


def Cal(request, year, month):
    calendar.setfirstweekday(calendar.SUNDAY)
    prev_year = int(year)
    next_year = int(year)
    prev_month = int(month) - 1
    next_month = int(month) + 1
    if prev_month == 0:
        prev_year -= 1
        prev_month = 12
    if next_month == 13:
        next_year += 1
        next_month = 1
    month_cal = calendar.monthcalendar(int(year), int(month))
    print(month_cal)
    events = Event.objects.filter(year=year, month=month)
    print(events)
    return render(request, "events/calendar.html", {
                                                "month_cal": month_cal,
                                                "prev_month": prev_month,
                                                "next_month": next_month,
                                                "prev_year": prev_year,
                                                "next_year": next_year,
                                                "events": events,
                                            })
