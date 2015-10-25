from django.contrib import admin
from .models import CofifiUser
from message.models import Message
from cofipy_app.models import QuoteIdea
from friends.models import FriendRequest

class SentMessageAdmin(admin.StackedInline):
	model = Message
	fk_name = "sender"
	extra = 0
	verbose_name = "Sent message"
class ReceivedMessageAdmin(admin.StackedInline):
	model = Message
	fk_name = "receiver"
	extra = 0
	verbose_name = "Received message"
class QuoteIdeaAdmin(admin.StackedInline):
	model = QuoteIdea
	fk_name = "creator"
	extra = 0
	verbose_name = "Quote Idea"
class FriendsRequestSentAdmin(admin.StackedInline):
	model = FriendRequest
	fk_name = "sender"
	extra = 0
	verbose_name = "FriendRequests_sent"
class FriendsRequestReceivedAdmin(admin.StackedInline):
	model = FriendRequest
	fk_name = "receiver"
	extra = 0
	verbose_name = "FriendRequests_received"
class CofifiUserAdmin(admin.ModelAdmin):
	inlines = [ SentMessageAdmin , ReceivedMessageAdmin, QuoteIdeaAdmin,FriendsRequestSentAdmin,FriendsRequestReceivedAdmin]

admin.site.register(CofifiUser, CofifiUserAdmin)