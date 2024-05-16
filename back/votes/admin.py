from django.contrib import admin
from .models import Order, Bid, Settings

# Register your models here.
admin.site.register(Order)
admin.site.register(Bid)
admin.site.register(Settings)