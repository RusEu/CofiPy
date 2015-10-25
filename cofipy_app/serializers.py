#Serializers 

from user_profile.models import CofifiUser
from .models import QuoteIdea

from django.contrib.auth.models import User
from django.contrib import auth
from django.core.context_processors import request

from rest_framework import routers, serializers, viewsets

#CofifiUser model Serializer

def get_current(request):
    return request.user

class CofifiSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source='user.username')
    class Meta:
        model = CofifiUser
        fields = ('user','image')

class CofifiFriendSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    friends = CofifiSerializer(many=True)

    class Meta:
        model = CofifiUser
        fields = ('user','birth_date','bio','image','gender','friends')

class CofifiViewSet(viewsets.ModelViewSet):
    queryset = CofifiUser.objects.all()
    serializer_class = CofifiFriendSerializer
# User model Serializer

class UserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        userid = self.request.user
        return CofifiUser.objects.filter(user=userid)
    serializer_class = CofifiFriendSerializer

# QuoteIdea model Serializer

class QuoteSerializer(serializers.ModelSerializer):
    current_user = serializers.SerializerMethodField()
    creator = serializers.CharField(source='creator.user.username')
    votes_received = CofifiSerializer(many=True)
    image = serializers.CharField(source='creator.image')

    def get_current_user(self,foo):
        request = self.context.get('request', None)
        return str(request.user)

    class Meta:
        model = QuoteIdea
        fields = ('id','creator','current_user','image','text','votes','created_at','votes_received')

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = QuoteIdea.objects.all()
    serializer_class = QuoteSerializer
