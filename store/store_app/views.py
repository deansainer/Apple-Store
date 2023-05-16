from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store_app/store.html', context)


def cart(request):
    return render(request, 'store_app/cart.html')


def checkout(request):
    return render(request, 'store_app/checkout.html')


def thanks(request):
    return render(request, 'store_app/thanks_page.html')