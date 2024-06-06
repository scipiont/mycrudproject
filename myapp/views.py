from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_list.html', {'clients': clients})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'myapp/client_detail.html', {'client': client})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'myapp/order_detail.html', {'order': order})