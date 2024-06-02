from django import forms
from .models import PurchaseOrderTracker

# class PurchaseFilterForm(forms.Form):
#     category_id = forms.CharField()

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderTracker
        fields = ['product', 'purchase_order_number', 'amount', 'category_id']
        widgets = {
            'product': forms.TextInput(attrs={'placeholder': 'Product Name'}),
            'purchase_order_number': forms.TextInput(attrs={'placeholder': 'Purchase Order Number'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Amount'}),
            'category_id': forms.Select(attrs={'placeholder': 'Category'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_id'].widget = forms.Select(choices=PurchaseOrderTracker.Category.choices)

