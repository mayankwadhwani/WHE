import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Event(models.Model):
    title = models.CharField('Title', max_length=140)
    location = models.CharField('Location', max_length=140)
    info = models.TextField()
    starts = models.DateTimeField('Starts')
    ends = models.DateTimeField('Ends')
    arrive_when = models.DateTimeField('Arrival Time', null=True, blank=True)
    arrive_where = models.CharField(
        'Arrival location', null=True, blank=True, max_length=150)
    registration_starts = models.DateTimeField('Registration Starts')
    registration_limit = models.IntegerField('Guest Limit',
                                             default=0,
                                             choices=[(0, u"No limit")] + list(zip(range(1, 100), range(1, 100))))
    
    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"
        ordering = ['-starts']

    def __str__(self):
        if self.starts.date() != self.ends.date():
            return u"%s, %s - %s" % (self.title,
                            self.starts.strftime("%a %H:%M"),
                            self.ends.strftime("%a %H:%M"))
        else:
            return u"%s, %s - %s" % (self.title,
                            self.starts.strftime("%H:%M"),
                            self.ends.strftime("%H:%M"))

    def get_absolute_url(self):
        return reverse('events', args=[str(self.pk)])