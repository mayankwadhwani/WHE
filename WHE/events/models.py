import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year+4)]
CURRENT_YEAR = datetime.date.today().year

MONTH_CHOICES = [(r, r) for r in range(1, 13)]
CURRENT_MONTH = datetime.date.today().month

DAY_CHOICES = [(r, r) for r in range(1, 31)]
CURRENT_DAY = datetime.date.today().day


class Event(models.Model):
    title = models.CharField('Title', max_length=140)
    location = models.CharField('Location', max_length=140)
    info = models.TextField()
    year = models.IntegerField(
        ('year'), choices=YEAR_CHOICES, default=CURRENT_YEAR)
    month = models.IntegerField(
        ('month'), choices=MONTH_CHOICES, default=CURRENT_MONTH)
    day = models.IntegerField(
        ('day'), choices=DAY_CHOICES, default=CURRENT_DAY)
    starts = models.DateTimeField('Starts')
    ends = models.DateTimeField('Ends')
    arrive_when = models.DateTimeField('Arrival Time', null=True, blank=True)
    arrive_where = models.CharField(
        'Arrival location', null=True, blank=True, max_length=150)
    registration_starts = models.DateTimeField('Registration Starts')
    registration_limit = models.IntegerField('Guest Limit',
                                             default=0,
                                             choices=[(0, u"No limit")] + list(zip(range(1, 100), range(1, 100))))
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True,
                                blank=True)


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
