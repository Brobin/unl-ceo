from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
    title = models.CharField(max_length=128)
    uploaded = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User)


class Image(Upload):
    image = models.ImageField(upload_to = 'images')

    def thumbnail(self):
        return '<img src="%s" style="height:80px;"/>' % self.image.url
    thumbnail.short_description = 'thumbnail'
    thumbnail.allow_tags = True

    def __str__(self):
        return 'Image: %s' % self.image


class Document(Upload):
    document = models.FileField(upload_to = 'documents')

    def __str__(self):
        return 'Document: %s' % self.document
