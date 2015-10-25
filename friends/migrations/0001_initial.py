# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(related_name='friend_request_receiver', to='user_profile.CofifiUser')),
                ('sender', models.ForeignKey(related_name='friend_request_sender', to='user_profile.CofifiUser')),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friends', models.ManyToManyField(related_name='friends_username', to='user_profile.CofifiUser')),
                ('username', models.ForeignKey(related_name='username_friend', to='user_profile.CofifiUser')),
            ],
        ),
    ]
