# from django.shortcuts import render, get_object_or_404
# from .models import Client, Product, Order

# def client_list(request):
#     clients = Client.objects.all()
#     return render(request, 'myapp/client_list.html', {'clients': clients})

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'myapp/product_list.html', {'products': products})

# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, 'myapp/order_list.html', {'orders': orders})

# def client_detail(request, client_id):
#     client = get_object_or_404(Client, id=client_id)
#     return render(request, 'myapp/client_detail.html', {'client': client})

# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'myapp/product_detail.html', {'product': product})

# def order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request, 'myapp/order_detail.html', {'order': order})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm

# Client Views
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_list.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'myapp/client_detail.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'myapp/client_form.html', {'form': form})

def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'myapp/client_form.html', {'form': form})

def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'myapp/client_confirm_delete.html', {'client': client})

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/product_form.html', {'form': form})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'myapp/product_confirm_delete.html', {'product': product})

# Order Views
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'myapp/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'myapp/order_form.html', {'form': form})

def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'myapp/order_form.html', {'form': form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'myapp/order_confirm_delete.html', {'order': order})