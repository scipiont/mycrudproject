# from django import forms
# from .models import Client, Product, Order

# class ClientForm(forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = ['name', 'email', 'phone_number', 'address', 'registration_date']

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'price', 'quantity', 'date_added']

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['client', 'products', 'total_amount', 'order_date']

from django import forms
from .models import Client, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'address', 'registration_date']
        labels = {
            'name': 'Имя клиента',
            'email': 'Электронная почта клиента',
            'phone_number': 'Номер телефона клиента',
            'address': 'Адрес клиента',
            'registration_date': 'Дата регистрации клиента',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'date_added']
        labels = {
            'name': 'Название товара',
            'description': 'Описание товара',
            'price': 'Цена товара',
            'quantity': 'Количество товара',
            'date_added': 'Дата добавления товара',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount', 'order_date']
        labels = {
            'client': 'Клиент',
            'products': 'Товары',
            'total_amount': 'Количество заказа',
            'order_date': 'Дата оформления заказа',
        }