# from django.db import models
# from django.utils import timezone

# class Client(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20)
#     address = models.TextField()
#     registration_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField()
#     date_added = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
#     products = models.ManyToManyField(Product, related_name='orders')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"Order {self.id} by {self.client.name}"

from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя клиента')
    email = models.EmailField(unique=True, verbose_name='Электронная почта клиента')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона клиента')
    address = models.TextField(verbose_name='Адрес клиента')
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации клиента')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    date_added = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления товара')
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True, verbose_name='Фотография товара')

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    products = models.ManyToManyField(Product, related_name='orders', verbose_name='Товары')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая сумма заказа')
    order_date = models.DateTimeField(default=timezone.now, verbose_name='Дата оформления заказа')

    def __str__(self):
        return f"Заказ {self.id} от {self.client.name}"