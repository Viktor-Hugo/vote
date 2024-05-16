from django.http import JsonResponse
from .models import Settings
# utils.py
from .models import Bid, AnnouncementResult

def calculate_winners():
    # 모든 발표 순서에 대해 최상위 입찰을 찾음
    all_bids = Bid.objects.all().order_by('-payment')
    bids_by_order = {}

    for bid in all_bids:
        if bid.order.id not in bids_by_order:
            bids_by_order[bid.order.id] = []
        bids_by_order[bid.order.id].append(bid)

    winners = {}
    team_highest_bids = {}
    
    # 각 발표 순서에 대해 최상위 입찰팀 선정
    for order, bids in bids_by_order.items():
        for bid in bids:
            if bid.team not in team_highest_bids:
                team_highest_bids[bid.team] = bid
                winners[order] = bid
                break
            else:
                # 현재 팀이 이미 다른 발표 순서를 낙찰받은 경우, 더 높은 금액 비교
                current_highest_bid = team_highest_bids[bid.team]
                if bid.payment > current_highest_bid.payment:
                    # 기존의 낮은 금액 낙찰 취소
                    del winners[current_highest_bid.order.id]
                    winners[order] = bid
                    team_highest_bids[bid.team] = bid
                    break

    # 낙찰 결과를 AnnouncementResult에 저장
    AnnouncementResult.objects.all().delete()  # 기존 결과 삭제
    for order, bid in winners.items():
        AnnouncementResult.objects.create(announcement_order=order, winning_team=bid.team)

    # 남은 발표 순서 채우기
    for order, bids in bids_by_order.items():
        if order not in winners:
            for bid in bids:
                if bid.team not in team_highest_bids:
                    AnnouncementResult.objects.create(announcement_order=order, winning_team=bid.team)
                    team_highest_bids[bid.team] = bid
                    break

    return winners






def check_deadline(func):
    def wrapper(request, *args, **kwargs):
        try:
            settings = Settings.objects.first()
            if settings and not settings.is_active:
                return JsonResponse({"data": "마감"}, status=406)
        except Settings.DoesNotExist:
            return JsonResponse({"data": "setting이 정의 되지 않음."})
        return func(request, *args, **kwargs)
    return wrapper
