from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.utils.html import strip_tags


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(default='', blank=True, max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    tags = TaggableManager()

    def __str__(self):
        return '{0} - {1}'.format(self.created, self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def preview(self):
        try:
            preview = strip_tags(self.content)[:400]
        except:
            preview = ''
        return preview + '...'
    preview.short_description = 'content'

    def get_date(self):
        return self.created
    get_date.short_description = 'date'

    @property
    def url(self):
        return '/blog/{0}/{1}/{2}'.format(self.created.year,  self.created.month, self.slug)

    @property
    def html_url(self):
        return '<a href="{0}">{1}</a>'.format(self.url, self.title)

    def get_absolute_url(self):
        return self.url
