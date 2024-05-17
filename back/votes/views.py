from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Order, Bid, Settings, AnnouncementResult
from .serializers import OrderListSerializer, BidSerializer, AnnouncementResultSerializer
from .utils import check_deadline, calculate_winners

User = get_user_model()

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    orders = Order.objects.all()
    serializer = OrderListSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@check_deadline
def bid(request, order_pk):
    user = request.user
    payment = int(request.data.get('payment'))
    order = get_object_or_404(Order, pk=order_pk)
    is_bid_success = False

    if user.score < payment:
        return Response({'data': '보유 금액 부족', 'balance': user.score}, status=status.HTTP_400_BAD_REQUEST)
    elif payment <= order.price:
        return Response({'data': '구매 가능 금액 미달', 'price': order.price}, status=status.HTTP_400_BAD_REQUEST)

    # 본인 입찰 갱신
    if order in user.orders.all():
        older_bid = Bid.objects.get(team=user, order=order)
        user.score += older_bid.payment
        print(older_bid.payment)
        print(user.score)
        order.teams.remove(user)

        if user.score >= payment > order.price:
            user.score -= payment
            order.price = payment
            serialzer = BidSerializer(data=request.data)
            if serialzer.is_valid(raise_exception=True):
                serialzer.save(team=user, order=order)
        
        is_bid_success = True
        user.save()
        order.save()
    # 최초 입찰
    elif user.score >= payment > order.price:
        serialzer = BidSerializer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save(team=user, order=order)
        order.price = payment
        user.score -= payment
        user.save()
        order.save()
        is_bid_success = True
    
    data = {
            'success': True,
            'balance': user.score,
            'order': OrderListSerializer(order).data,
            # 'teams': order.teams.all()
        }
    if is_bid_success:
        return Response(data, status=status.HTTP_200_OK)
    else:
        data['success'] = False
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@check_deadline
def bid_cancle(request, order_pk):
    user = request.user
    order = get_object_or_404(Order, pk=order_pk)
    bid = Bid.objects.filter(order=order).latest('payment')
    if bid.team == user:
        return Response({'data': '최상위 입찰자는 입찰 취소가 불가능 합니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    elif user.orders.exists():
        bid = Bid.objects.get(team=user.pk, order=order_pk)
        user.score += bid.payment
        order.teams.remove(user)
        user.save()
        data = {
            'success': True,
            'refundAmount': bid.payment,
            'balance': user.score,
            'lastBidPayment': order.price
        }
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deadline(request):
    if request.user.is_superuser:
        setting = Settings.objects.first()
        setting.is_active = not setting.is_active
        setting.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def winner(request):
    if request.user.is_superuser:
        calculate_winners()
        results = AnnouncementResult.objects.all().order_by('announcement_order')
        serializer = AnnouncementResultSerializer(results, many=True)
        remain_teams = serializer.data[0]['remain_teams']
        data = {
            'remain_teams': [],
            'data': serializer.data
        }
        for d in serializer.data:
            del d['remain_teams']
        for team in remain_teams:
            user = User.objects.get(pk=team)
            data['remain_teams'].append({team: user.score})
        print(data)
        return Response(data)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)