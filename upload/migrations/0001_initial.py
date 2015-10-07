# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('upload_ptr', models.OneToOneField(auto_created=True, to='upload.Upload', parent_link=True, serialize=False, primary_key=True)),
                ('document', models.FileField(upload_to='docs')),
            ],
            bases=('upload.upload',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('upload_ptr', models.OneToOneField(auto_created=True, to='upload.Upload', parent_link=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='img')),
            ],
            bases=('upload.upload',),
        ),
        migrations.AddField(
            model_name='upload',
            name='uploaded_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
