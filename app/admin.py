from django.contrib import admin
from .models import PurchaseOrderTracker

class PurchaseOrderTrackerAdmin(admin.ModelAdmin):
    list_display = ('product', 'purchase_order_number', 'amount', 'purchase_order_id', 'category_id')
    list_filter = ('category_id',)
    search_fields = ('product', 'purchase_order_number', 'purchase_order_id')

admin.site.register(PurchaseOrderTracker, PurchaseOrderTrackerAdmin)
