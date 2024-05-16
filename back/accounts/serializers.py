from django.contrib.auth import get_user_model
from rest_framework import serializers
from votes.serializers import BidSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class UserBidSerialzer():
        class Meta(BidSerializer.Meta):
            read_only_fields = ('payment', ) + BidSerializer.Meta.read_only_fields
    
    orders = UserBidSerialzer()
    class Meta:
        model = User
        fields = ('id', 'username', 'orders', 'score')