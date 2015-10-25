from django.db import models
from user_profile.models import CofifiUser
# Create your models here.
class QuoteIdea(models.Model):
	creator = models.ForeignKey(CofifiUser,related_name="creator")
	text = models.TextField(max_length=250)
	votes = models.CharField(max_length=100,default="0")
	votes_received = models.ManyToManyField(CofifiUser)
	created_at = models.DateTimeField(auto_now_add=True)
	def get_current_user(self,request):
		return self.request.user
	def __unicode__(self):
		return  "Idea Posted By " + self.creator.user.username