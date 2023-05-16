from django.shortcuts import render
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    products = Product.objects.all()
    context = {'products': products, 'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    context = {'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    context = {'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/checkout.html', context)


def thanks(request):
    return render(request, 'store_app/thanks_page.html')