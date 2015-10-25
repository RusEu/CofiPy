# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteIdea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=250)),
                ('votes', models.CharField(default=b'0', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(related_name='creator', to='user_profile.CofifiUser')),
                ('votes_received', models.ManyToManyField(to='user_profile.CofifiUser')),
            ],
        ),
    ]
