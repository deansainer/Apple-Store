from django.shortcuts import render


def store(request):
    return render(request, 'store_app/store.html')


def cart(request):
    return render(request, 'store_app/cart.html')


def checkout(request):
    return render(request, 'store_app/checkout.html')


def thanks(request):
    return render(request, 'store_app/thanks_page.html')