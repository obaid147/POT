from django.db import models
from datetime import datetime

class PurchaseOrderTracker(models.Model):

    class Category(models.TextChoices):
        cat_A = 'A'
        cat_B = 'B'
        cat_C = 'C'
        cat_D = 'D'

    id = models.IntegerField(primary_key=True)
    product = models.CharField(max_length=225)
    purchase_order_number = models.CharField(max_length=225)
    amount = models.FloatField(max_length=5)
    category_id = models.CharField(max_length=1, choices=Category.choices, default='A')
    purchase_order_id = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if object is being created (not updated)
            # Get the count of existing purchase orders for the same category
            existing_count = PurchaseOrderTracker.objects.filter(category_id=self.category_id).count() + 1

            # Format the purchase order ID
            purchase_order_id = f"{datetime.now().strftime('%Y%m%d')}{self.category_id}{existing_count:03d}"

            # Assign the generated purchase order ID to the object
            self.purchase_order_id = purchase_order_id

        super().save(*args, **kwargs)
