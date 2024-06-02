from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.create_purchase_order, name="create_purchase_order"),
    path("create/", views.create_purchase_order, name="create_purchase_order"),
    path("signup/", views.signup, name="signup")
]