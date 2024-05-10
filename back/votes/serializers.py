from rest_framework import serializers
from .models import Order, Bid


class OrderListSerializers(serializers.ModelSerializer):
    last_bid_team = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_last_bid_team(self, obj):
        c_records = Bid.objects.filter(order=obj)  # A와 관계된 C 레코드들 가져오기
        if c_records:
            max_k = max(c_records, key=lambda c: c.payment)  # C 레코드들 중 k 필드의 최대값 찾기
            class BidUserSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Bid
                    fields = ('team', )
            return BidUserSerializer(max_k).data['team']
        return None  # A와 관련된 C 레코드가 없을 경우 None 반환

class BidSerializers(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ('payment', )
        read_only_fields = ('team', 'order')
