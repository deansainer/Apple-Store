import json
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .forms import *

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
    categories = Category.objects.all()
    context = {'categories': categories, 'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        if 'sort_by_price' in request.POST:
            items = order.orderitem_set.select_related('product').order_by('product__price')
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']

    context = {'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/cart.html', context)


def iphones(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    products = Product.objects.all().filter(category=1)
    context = {'products': products, 'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/iphone.html', context)


def macs(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    products = Product.objects.all().filter(category=2)
    context = {'products': products, 'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/mac.html', context)


def ipads(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    products = Product.objects.all().filter(category=4)
    context = {'products': products, 'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/ipad.html', context)


def airpods(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    products = Product.objects.all().filter(category=5)
    context = {'products': products, 'items': items, 'order': order, 'cart_quantity': cart_quantity}
    return render(request, 'store_app/airpods.html', context)


def confirm_order(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ShippingAddressForm()
    return render(request, 'store_app/thanks.html', {'form': form})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
        if request.method == 'POST':
            form = ShippingAddressForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('http://127.0.0.1:8000/thanks/')
        else:
            form = ShippingAddressForm()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    context = {'items': items, 'order': order, 'cart_quantity': cart_quantity, 'form': form}
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

def product_info(request, slug):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
        cart_quantity = order['get_cart_quantity']
    product = Product.objects.get(slug=slug)
    context = {'items': items, 'order': order, 'cart_quantity': cart_quantity, 'product': product}
    return render(request, 'store_app/product_info.html', context)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
