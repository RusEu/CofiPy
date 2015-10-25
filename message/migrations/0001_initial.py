# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chat_id', models.CharField(max_length=10)),
                ('message', models.TextField(null=True, blank=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('username', models.ForeignKey(related_name='username', to='user_profile.CofifiUser')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('receiver', models.ForeignKey(related_name='received_messages', to='user_profile.CofifiUser')),
                ('sender', models.ForeignKey(related_name='sent_messages', to='user_profile.CofifiUser')),
            ],
        ),
    ]
