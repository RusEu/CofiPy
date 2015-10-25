from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

GENDER_CHOICES = (
	("M" , "Male"),
	("F" , "Female"),
	)

class CofifiUser(models.Model):
	user = models.OneToOneField(User)
	friends = models.ManyToManyField('self',related_name="user_friends",blank = True)
	bio = models.TextField(default="")
	image = models.ImageField(upload_to="user")
	country =  CountryField()
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
	birth_date= models.DateField()
	def __unicode__(self):
		return self.user.username
