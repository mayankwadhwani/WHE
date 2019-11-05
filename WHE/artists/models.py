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
    youtube = models.TextField('YouTube', null=True, blank=True)
    mediaKitLink = models.TextField('Media Kit', null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True,
                                blank=True)
    short_description = models.CharField('Short Description', max_length=50)

    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artists', args=[str(self.pk)])
