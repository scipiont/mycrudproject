
# from django.contrib import admin
# from django.http import HttpResponse
# from .models import Client, Product, Order
# import csv
# from reportlab.lib.pagesizes import letter, landscape
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics

# # Регистрация шрифта DejaVuSans
# pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

# # Действия для выгрузки данных в CSV
# def export_clients_csv(modeladmin, request, queryset):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=clients.csv'
#     response.write('\ufeff'.encode('utf8'))  # Добавляем BOM для корректного отображения в Excel
#     writer = csv.writer(response)
#     writer.writerow(['ID', 'Имя', 'Электронная почта', 'Номер телефона', 'Адрес', 'Дата регистрации'])
#     for client in queryset:
#         writer.writerow([client.id, client.name, client.email, client.phone_number, client.address, client.registration_date])
#     return response

# export_clients_csv.short_description = 'Экспорт в CSV'

# def export_products_csv(modeladmin, request, queryset):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=products.csv'
#     response.write('\ufeff'.encode('utf8'))  # Добавляем BOM для корректного отображения в Excel
#     writer = csv.writer(response)
#     writer.writerow(['ID', 'Название', 'Описание', 'Цена', 'Количество', 'Дата добавления'])
#     for product in queryset:
#         writer.writerow([product.id, product.name, product.description, product.price, product.quantity, product.date_added])
#     return response

# export_products_csv.short_description = 'Экспорт в CSV'

# def export_orders_csv(modeladmin, request, queryset):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=orders.csv'
#     response.write('\ufeff'.encode('utf8'))  # Добавляем BOM для корректного отображения в Excel
#     writer = csv.writer(response)
#     writer.writerow(['ID', 'Клиент', 'Общая сумма', 'Дата заказа'])
#     for order in queryset:
#         writer.writerow([order.id, order.client.name, order.total_amount, order.order_date])
#     return response

# export_orders_csv.short_description = 'Экспорт в CSV'

# # Действия для выгрузки данных в PDF
# def export_clients_pdf(modeladmin, request, queryset):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=clients.pdf'
#     p = canvas.Canvas(response, pagesize=landscape(letter))
#     p.setFont('DejaVuSans', 12)
#     p.drawString(100, 550, "Клиенты")
#     y = 520
#     for client in queryset:
#         p.drawString(100, y, f"ID: {client.id}, Имя: {client.name}, Электронная почта: {client.email}, Телефон: {client.phone_number}, Адрес: {client.address}, Дата регистрации: {client.registration_date}")
#         y -= 20
#     p.showPage()
#     p.save()
#     return response

# export_clients_pdf.short_description = 'Экспорт в PDF'

# def export_products_pdf(modeladmin, request, queryset):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=products.pdf'
#     p = canvas.Canvas(response, pagesize=landscape(letter))
#     p.setFont('DejaVuSans', 12)
#     p.drawString(100, 550, "Товары")
#     y = 520
#     for product in queryset:
#         p.drawString(100, y, f"ID: {product.id}, Название: {product.name}, Описание: {product.description}, Цена: {product.price}, Количество: {product.quantity}, Дата добавления: {product.date_added}")
#         y -= 20
#     p.showPage()
#     p.save()
#     return response

# export_products_pdf.short_description = 'Экспорт в PDF'

# def export_orders_pdf(modeladmin, request, queryset):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=orders.pdf'
#     p = canvas.Canvas(response, pagesize=landscape(letter))
#     p.setFont('DejaVuSans', 12)
#     p.drawString(100, 550, "Заказы")
#     y = 520
#     for order in queryset:
#         p.drawString(100, y, f"ID: {order.id}, Клиент: {order.client.name}, Общая сумма: {order.total_amount}, Дата заказа: {order.order_date}")
#         y -= 20
#     p.showPage()
#     p.save()
#     return response

# export_orders_pdf.short_description = 'Экспорт в PDF'

# # Регистрация моделей и добавление действий
# class ClientAdmin(admin.ModelAdmin):
#     actions = [export_clients_csv, export_clients_pdf]

# class ProductAdmin(admin.ModelAdmin):
#     actions = [export_products_csv, export_products_pdf]

# class OrderAdmin(admin.ModelAdmin):
#     actions = [export_orders_csv, export_orders_pdf]

# admin.site.register(Client, ClientAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Order, OrderAdmin)

from django.contrib import admin
from django.http import HttpResponse
from .models import Client, Product, Order
import csv
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import simpleSplit

# Регистрация шрифта DejaVuSans
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

# Действия для выгрузки данных в CSV
def export_clients_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=clients.csv'
    response.write('\ufeff'.encode('utf8'))  # Добавляем BOM для корректного отображения в Excel
    writer = csv.writer(response)
    writer.writerow(['ID', 'Имя', 'Электронная почта', 'Номер телефона', 'Адрес', 'Дата регистрации'])
    for client in queryset:
        writer.writerow([client.id, client.name, client.email, client.phone_number, client.address, client.registration_date])
    return response

export_clients_csv.short_description = 'Экспорт в CSV'

def export_products_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    response.write('\ufeff'.encode('utf8'))  # Добавляем BOM для корректного отображения в Excel
    writer = csv.writer(response)
    writer.writerow(['ID', 'Название', 'Описание', 'Цена', 'Количество', 'Дата добавления'])
    for product in queryset:
        writer.writerow([product.id, product.name, product.description, product.price, product.quantity, product.date_added])
    return response

export_products_csv.short_description = 'Экспорт в CSV'

def export_orders_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=orders.csv'
    response.write('\ufeff'.encode('utf8'))  # Добавляем BOM для корректного отображения в Excel
    writer = csv.writer(response)
    writer.writerow(['ID', 'Клиент', 'Общая сумма', 'Дата заказа'])
    for order in queryset:
        writer.writerow([order.id, order.client.name, order.total_amount, order.order_date])
    return response

export_orders_csv.short_description = 'Экспорт в CSV'

# Функция для добавления текста с переносом строк
def draw_wrapped_text(canvas, text, x, y, max_width):
    lines = simpleSplit(text, 'DejaVuSans', 12, max_width)
    for line in lines:
        canvas.drawString(x, y, line)
        y -= 14  # Высота строки
    return y

# Действия для выгрузки данных в PDF
def export_clients_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=clients.pdf'
    p = canvas.Canvas(response, pagesize=landscape(letter))
    p.setFont('DejaVuSans', 12)
    y = 550
    p.drawString(10, y, "Клиенты")
    y -= 20
    for client in queryset:
        text = f"ID: {client.id}, Имя: {client.name}, Электронная почта: {client.email}, Телефон: {client.phone_number}, Адрес: {client.address}, Дата регистрации: {client.registration_date}"
        y = draw_wrapped_text(p, text, 10, y, 750)
        y -= 10
    p.showPage()
    p.save()
    return response

export_clients_pdf.short_description = 'Экспорт в PDF'

def export_products_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=products.pdf'
    p = canvas.Canvas(response, pagesize=landscape(letter))
    p.setFont('DejaVuSans', 12)
    y = 550
    p.drawString(10, y, "Товары")
    y -= 20
    for product in queryset:
        text = f"ID: {product.id}, Название: {product.name}, Описание: {product.description}, Цена: {product.price}, Количество: {product.quantity}, Дата добавления: {product.date_added}"
        y = draw_wrapped_text(p, text, 10, y, 750)
        y -= 10
    p.showPage()
    p.save()
    return response

export_products_pdf.short_description = 'Экспорт в PDF'

def export_orders_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=orders.pdf'
    p = canvas.Canvas(response, pagesize=landscape(letter))
    p.setFont('DejaVuSans', 12)
    y = 550
    p.drawString(10, y, "Заказы")
    y -= 20
    for order in queryset:
        text = f"ID: {order.id}, Клиент: {order.client.name}, Общая сумма: {order.total_amount}, Дата заказа: {order.order_date}"
        y = draw_wrapped_text(p, text, 10, y, 750)
        y -= 10
    p.showPage()
    p.save()
    return response

export_orders_pdf.short_description = 'Экспорт в PDF'

# Регистрация моделей и добавление действий
class ClientAdmin(admin.ModelAdmin):
    actions = [export_clients_csv, export_clients_pdf]

class ProductAdmin(admin.ModelAdmin):
    actions = [export_products_csv, export_products_pdf]

class OrderAdmin(admin.ModelAdmin):
    actions = [export_orders_csv, export_orders_pdf]

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)