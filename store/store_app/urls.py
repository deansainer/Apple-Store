from django.urls import path, include
from rest_framework import routers

from .views import *
from . import views


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', views.store, name='store_page'),
    path('cart/', views.cart, name='cart_page'),
    path('checkout/', views.checkout, name='checkout_page'),
    path('thanks/', views.thanks, name='thanks_page'),
    path('update_item/', views.updateItem, name='update_item'),
    path('api/', include(router.urls)),
    path('iphone/', views.iphones, name='iphone'),
    path('mac/', views.macs, name='mac'),
    path('ipad/', views.ipads, name='ipad'),
    path('airpods/', views.airpods, name='airpods'),


]

