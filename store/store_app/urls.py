from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.store, name='store_page'),
    path('cart/', views.cart, name='cart_page'),
    path('checkout/', views.checkout, name='checkout_page'),

]