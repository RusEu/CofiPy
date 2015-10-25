from django.shortcuts import render,render_to_response
from django.core.context_processors import request
from django.core.context_processors import csrf
from django.template import RequestContext
from cofipy_app.models import QuoteIdea
from user_profile.models import CofifiUser
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count
# Create your views here.

def userprofile(request,pk):
	page_range = range(0,9)
	quotes= QuoteIdea.objects.all().filter(creator__user=pk).order_by('-id')[:6]
	userprofile = CofifiUser.objects.get(user=pk)
	all_quotes = QuoteIdea.objects.all().filter(creator__user=pk)
	mostvoted = QuoteIdea.objects.all().order_by('-votes')[:3]
	uzar = CofifiUser.objects.get(user = pk).friends.add(CofifiUser.objects.get(user = 4))
	friends = CofifiUser.objects.get(user=pk).friends.all()
	friends_image = CofifiUser.objects.get(user=pk).friends.all().order_by('?')[:6]
	context = {
		"page_range":page_range,
		"quotes":quotes,
		"mostvoted":mostvoted,
		"all_quotes":all_quotes,
		"userprofile":userprofile,
		"friends":friends,
		"friends_image":friends_image,
	}
	return render_to_response("userprofile.html",context,RequestContext(request))