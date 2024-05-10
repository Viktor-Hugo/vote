from django.contrib.auth import get_user_model
from rest_framework import serializers
from votes.serializers import BidSerializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class UserBidSerialzer():
        class Meta(BidSerializers.Meta):
            read_only_fields = ('payment', ) + BidSerializers.Meta.read_only_fields
    
    orders = UserBidSerialzer()
    class Meta:
        model = User
        fields = ('id', 'username', 'orders', 'score')