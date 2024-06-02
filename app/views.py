from typing import Any
from django.shortcuts import render, redirect
from app.models import PurchaseOrderTracker
from django.contrib import messages
from .forms import PurchaseOrderForm
from django.contrib.auth.decorators import login_required

# admin admin
@login_required # for this to work, url pattern must have the "accounts/" as the route in main url file
def index(request):
    if not request.user.is_authenticated: # will use this once auth part is fully done
        return redirect('login.html')
    context = {
        #'form': PurchaseFilterForm(), 
        'orders': PurchaseOrderTracker.objects.all().order_by('category_id')
        }
    return render(request, 'index.html', context)

# admin admin
@login_required
def create_purchase_order(request):
    if not request.user.is_authenticated: # will use this once auth part is fully done
        return redirect('login.html')
    error_message = None
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            instance = form.save()
            category_id = instance.get_category_id_display()
            error_message = f'New category ID created: {category_id}'
            messages.success(request, error_message)
            return redirect('create_purchase_order')
    else:
        form = PurchaseOrderForm
    return render(request, 'create_purchase_order.html', {'form': form, 'orders': PurchaseOrderTracker.objects.all().order_by('category_id')})

# signup
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

