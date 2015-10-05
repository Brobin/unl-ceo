from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Page(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(default='', blank=True, max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    script = models.TextField(default='', blank=True)
    style = models.TextField(default='', blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    @property
    def url(self):
        return '/{0}'.format(self.slug)

    def get_absolute_url(self):
        return self.url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
