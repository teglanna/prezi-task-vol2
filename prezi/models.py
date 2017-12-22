from django.db import models


class Creator(models.Model):
    name = models.CharField('creator name', max_length=200)
    profile_url = models.URLField('creator profile', max_length=200)


class Prezi(models.Model):
    id = models.CharField('id', max_length=200, primary_key=True)
    title = models.CharField('title', max_length=200)
    thumbnail = models.URLField('thumbnail', max_length=200)
    creator = models.ForeignKey(Creator, verbose_name='creator', related_name='prezis')
    created_on = models.DateField('created on', blank=True, null=True)
