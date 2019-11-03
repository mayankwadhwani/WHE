import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField('Artist Name', max_length=140)
    about = models.TextField('About', null=True, blank=True)
    facebook = models.TextField('Facebook', null=True, blank=True)
    twitter = models.TextField('Twitter', null=True, blank=True)
    instagram = models.TextField('Instagram', null=True, blank=True)
    youtube = models.TextField('Instagram', null=True, blank=True)
    mediaKitLink = models.TextField('Instagram', null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True,
                                blank=True)

    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists"

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
        return reverse('artists', args=[str(self.pk)])
