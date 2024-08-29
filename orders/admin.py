from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductAdminInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductAdminInline
    ]


admin.site.register(Order, OrderAdmin)