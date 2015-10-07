from django.db import models
from django.conf import settings
from django.template.defaultfilters import date
from django.utils.html import strip_tags


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=256)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def seconds(self):
        return (self.end - self.start).total_seconds()

    @property
    def minutes(self):
        return float(self.seconds) / 60

    @property
    def hours(self):
        return float(self.seconds) / 3600

    def preview(self):
        try:
            preview = strip_tags(self.description)[:64]
        except:
            preview = ''
        return preview + '...'
    preview.short_description = 'preview'

    def __str__(self):
        return '%s: %s - %s' % (
            self.title,
            date(self.start, settings.DATETIME_FORMAT),
            date(self.end, settings.DATETIME_FORMAT),
        )