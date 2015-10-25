from django.db import models
from user_profile.models import CofifiUser
# Create your models here.

class FriendRequest(models.Model):
	sender = models.ForeignKey(CofifiUser,related_name="friend_request_sender")
	receiver = models.ForeignKey(CofifiUser,related_name="friend_request_receiver")
	confirmed = models.BooleanField(default=False)
	def __unicode__(self):
		return  self.sender.user.username + " -> " + self.receiver.user.username

class Friendship(models.Model):
	username = models.ForeignKey(CofifiUser,related_name="username_friend")
	friends = models.ManyToManyField(CofifiUser,related_name="friends_username")
	def __unicode__(self):
		return  self.username.user.username