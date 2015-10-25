from .models import FriendRequest
from user_profile.models import CofifiUser

def friends_requests(request):
	try:
		receiver_id = request.user.id
		receiver = CofifiUser.objects.get( id = receiver_id )
		friends_requests = FriendRequest.objects.filter(receiver = receiver ).exclude( confirmed = True )
		return {"friends_requests":friends_requests}
	except CofifiUser.DoesNotExist:
		return {}
