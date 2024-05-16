from rest_framework import serializers
from .models import Order, Bid


class OrderListSerializers(serializers.ModelSerializer):
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

class BidSerializers(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ('payment', )
        read_only_fields = ('team', 'order')
