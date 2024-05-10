from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('bid/<int:order_pk>/', views.bid),
    path('bid/<int:order_pk>/cancle/', views.bid_cancle),
]
