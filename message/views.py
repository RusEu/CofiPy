from django.shortcuts import render,render_to_response
from message.models import Message,ChatRoom
from user_profile.models import CofifiUser
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django import template
from cofipy_app.models import QuoteIdea
from cofipy_app.forms import IdeaForm
import json
# Create your views here.
def index(request):
	username=request.user.id
	message= Message.objects.all().filter(receiver__user=username)
	i=0
	senders_list = []
	for item in message:
		senders_list.append(item.sender.user.username)
	senders = {}
	for e in senders_list:
		senders[e] = 1
	context={
	"message":message,
	"senders":senders,
	}
	receiver_list = {}
	return render_to_response("home.html",context,RequestContext(request))
def friend_message(request,friend):
	form = IdeaForm()
	username=request.user.id
	friend = str(friend)
	message= Message.objects.all().filter(receiver__user=username)
	i=0
	senders_list = []
	for item in message:
		senders_list.append(item.sender.user.username)
	senders = {}
	for e in senders_list:
		senders[e] = 1
	sender_id = User.objects.get(username = friend).pk
	cofifi_receiver_id = CofifiUser.objects.get(user = username)
	cofifi_sender_id = CofifiUser.objects.get(user = sender_id)
	receiver_id = username
	if request.method == "POST":
		for item in request.POST:
			print item
		text = request.POST.get('text')
		if receiver_id < sender_id:
			last_message_chat = ChatRoom.objects.create(chat_id=str(receiver_id)+"X"+str(sender_id),username=cofifi_receiver_id,message=text)
		else:
			last_message_chat = ChatRoom.objects.create(chat_id=str(sender_id)+"X"+str(receiver_id),username=cofifi_receiver_id,message=text)
	if receiver_id < sender_id:
		messages = ChatRoom.objects.filter(chat_id=str(receiver_id)+"X"+str(sender_id))
	else:
		messages = ChatRoom.objects.filter(chat_id=str(sender_id)+"X"+str(receiver_id))
	context={
	"form":form,
	"messages":messages,
	"senders":senders,
	"friend":friend,
	}
	return render_to_response("home.html",context,RequestContext(request))
def ajax(request,friend):
	form = IdeaForm()
	username=request.user.id
	friend = str(friend)
	message= Message.objects.all().filter(receiver__user=username)
	i=0
	senders_list = []
	for item in message:
		senders_list.append(item.sender.user.username)
	senders = {}
	for e in senders_list:
		senders[e] = 1
	print senders
	sender_id = User.objects.get(username = friend).pk
	cofifi_receiver_id = CofifiUser.objects.get(user = username)
	cofifi_sender_id = CofifiUser.objects.get(user = sender_id)
	receiver_id = username
	if request.method == "POST":
		print "Working"
		for item in request.POST:
			print item
		text = request.POST.get('send')
		if receiver_id < sender_id:
			last_message_chat = ChatRoom.objects.create(chat_id=str(receiver_id)+"X"+str(sender_id),username=cofifi_receiver_id,message=text)
		else:
			last_message_chat = ChatRoom.objects.create(chat_id=str(sender_id)+"X"+str(receiver_id),username=cofifi_receiver_id,message=text)
	if receiver_id < sender_id:
		messages = ChatRoom.objects.filter(chat_id=str(receiver_id)+"X"+str(sender_id))
	else:
		messages = ChatRoom.objects.filter(chat_id=str(sender_id)+"X"+str(receiver_id))
	context={
	"form":form,
	"messages":messages,
	"senders":senders,
	"friend":friend,
	}
	return render_to_response("ajax.html",context,RequestContext(request))
def json_message(request,friend):
	form = IdeaForm()
	username=request.user.id
	friend = str(friend)
	message= Message.objects.all().filter(receiver__user=username)
	i=0
	senders_list = []
	for item in message:
		senders_list.append(item.sender.user.username)
	senders = {}
	for e in senders_list:
		senders[e] = 1
	sender_id = User.objects.get(username = friend).pk
	cofifi_receiver_id = CofifiUser.objects.get(user = username)
	cofifi_sender_id = CofifiUser.objects.get(user = sender_id)
	receiver_id = username
	if request.method == "POST":
		for item in request.POST:
			print item
		text = request.POST.get('send')
		if receiver_id < sender_id:
			last_message_chat = ChatRoom.objects.create(chat_id=str(receiver_id)+"X"+str(sender_id),username=cofifi_receiver_id,message=text)
		else:
			last_message_chat = ChatRoom.objects.create(chat_id=str(sender_id)+"X"+str(receiver_id),username=cofifi_receiver_id,message=text)
	if receiver_id < sender_id:
		messages = ChatRoom.objects.filter(chat_id=str(receiver_id)+"X"+str(sender_id)).order_by('-time')
	else:
		messages = ChatRoom.objects.filter(chat_id=str(sender_id)+"X"+str(receiver_id)).order_by('-time')
	r = messages
	res = []
	for msgs in reversed(r) :
		res.append({'id':msgs.id,'user':str(msgs.username),'msg':msgs.message,'time':msgs.time.strftime('%I:%M:%S %p').lstrip('0')})
	data = json.dumps(res)
	context={
	"form":form,
	"messages":messages,
	"senders":senders,
	"friend":friend,
	}
	return HttpResponse(data,content_type="application/json")