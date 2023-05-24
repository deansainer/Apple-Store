import json
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

from .models import *
from django.http import JsonResponse


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


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer