from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order, Bid, AnnouncementResult


User = get_user_model()

class OrderListSerializer(serializers.ModelSerializer):
    last_bid_team = serializers.SerializerMethodField()
    teams = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_last_bid_team(self, obj):
        c_records = Bid.objects.filter(order=obj) 
        if c_records:
            max_k = max(c_records, key=lambda c: c.payment)
            class BidUserSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Bid
                    fields = ('team', )
            return BidUserSerializer(max_k).data['team']
        return None  
    
    def get_teams(self, obj):
        c_records = Bid.objects.filter(order=obj) 
        if c_records:
            sorted_k = sorted(c_records, key=lambda c: -c.payment)
            class BidUserSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Bid
                    fields = ('team', 'payment')
            return BidUserSerializer(sorted_k, many=True).data
        return None  

class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ('payment', )
        read_only_fields = ('team', 'order')


class AnnouncementResultSerializer(serializers.ModelSerializer):
    remain_teams = serializers.SerializerMethodField()

    def get_remain_teams(self, obj):
        users = User.objects.all() 
        results = AnnouncementResult.objects.all()
        if users and results: 
            filtered_k = [user for user in users if not user.announcementresult_set.exists()]
            sorted_k = sorted(filtered_k, key=lambda c: -c.score)
            return [user.id for user in sorted_k]
        return None  


    class Meta:
        model = AnnouncementResult
        fields = ('announcement_order', 'winning_team', 'remain_teams')
