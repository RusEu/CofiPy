from django.shortcuts import render,render_to_response
from user_profile.models import CofifiUser
from django.http import HttpResponseRedirect
from .models import FriendRequest

# Create your views here.
def index(request):
	return render_to_response("/templates/index.html")
def add_friend(request,pk):
	user_id = request.user.id
	username = CofifiUser.objects.get( id = user_id)
	friend = CofifiUser.objects.get( id = pk)
	username.friends.add(friend)
	username.save()
	friend_request = FriendRequest.objects.get( sender = friend ,receiver = username )
	friend_request.confirmed = True
	friend_request.save()

	url = request.META.get('HTTP_REFERER') + request.META.get('QUERY_STRING')
	return HttpResponseRedirect(url)