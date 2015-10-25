from django.shortcuts import render,render_to_response
from django.core.context_processors import request
from django.core.context_processors import csrf
from django.template import RequestContext
from .forms import IdeaForm
from .models import QuoteIdea
from friends.models import FriendRequest
from user_profile.models import CofifiUser
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count

# Create your views here.
#
Context= {}
Context.update(csrf(request))
@login_required
def index(request):
	all_quotes = QuoteIdea.objects.all().order_by('-id')[:12]
	context = {
		"all_quotes":all_quotes,
	}
	return render_to_response("index.html",
		context,
		RequestContext(request))
	
def post(request):
	if request.method == 'POST':
		form = IdeaForm(request.POST)
		if form.is_valid():
			name = request.user.username
			quote = "Default"
			quote = form.cleaned_data['idea']
			username= request.user
			username=username.id
        	post = QuoteIdea.objects.create(text=quote, creator=CofifiUser.objects.get(user=username))
        	success = True
	return HttpResponseRedirect("/")

def search(request):
	if request.GET:
		word = request.GET.get('word')
		list_usernames = {}
		search_list= CofifiUser.objects.all()
		for item in search_list:
			item_string = str(item)
			if word in item_string:
				list_usernames[item_string]=item.id
		page_range = range(0,9)
		context = {
			"page_range":page_range,
			"search_list":search_list,
			"list_usernames":list_usernames,
		}
		return render_to_response("search.html",
			context,
			RequestContext(request))
	else:
		HttpResponseRedirect("/")

def send_coffee(request,pk):
	username = request.user
	quote = QuoteIdea.objects.get(id=pk)
	votes = int(quote.votes) + 1
	QuoteIdea.objects.get(id=pk).votes_received.add(CofifiUser.objects.get(user = request.user.id))
	quote.votes = votes
	quote.save()
	url = request.META.get('HTTP_REFERER') + request.META.get('QUERY_STRING')
	return HttpResponseRedirect(url)

def homepage(request):
	print request.user
	page_range = range(0,9)
	username=request.user
	quotes= QuoteIdea.objects.all().filter(creator__user=username.id).order_by('-id')[:6]
	mostvoted = QuoteIdea.objects.all().order_by('-votes')[:3]
	userprofile = CofifiUser.objects.get(user=username.id)
	all_quotes = QuoteIdea.objects.all().filter(creator__user=username.id)
	uzar = CofifiUser.objects.get(user = username.id).friends.add(CofifiUser.objects.get(user = 4))
	friends = CofifiUser.objects.get(user=username.id).friends.all()
	context = {
		"page_range":page_range,
		"quotes":quotes,
		"mostvoted":mostvoted,
		"all_quotes":all_quotes,
		"userprofile":userprofile,
		"friends":friends,
	}
	return render_to_response("homepage.html",
		context,
		RequestContext(request))