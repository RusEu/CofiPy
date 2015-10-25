from django.db import models
from user_profile.models import CofifiUser
# Create your models here.
class Message(models.Model):
	sender = models.ForeignKey(CofifiUser,related_name="sent_messages")
	receiver = models.ForeignKey(CofifiUser,related_name="received_messages")
	text = models.TextField()
	time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return  "Message from " + self.sender.user.username + " to " + self.receiver.user.username

class ChatRoom(models.Model):
	chat_id = models.CharField(max_length = 10)
	username = models.ForeignKey(CofifiUser,related_name="username")
	message = models.TextField(blank=True,null=True)
	time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return  self.chat_id + " / " +self.username.user.username + " / " + str(self.time)  
