# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='friends',
            field=models.ManyToManyField(related_name='friends_username', to='user_profile.CofifiUser', blank=True),
        ),
    ]
