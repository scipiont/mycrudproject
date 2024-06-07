# from django.urls import path
# from . import views

# urlpatterns = [
#     path('clients/', views.client_list, name='client_list'),
#     path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
#     path('products/', views.product_list, name='product_list'),
#     path('products/<int:product_id>/', views.product_detail, name='product_detail'),
#     path('orders/', views.order_list, name='order_list'),
#     path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:client_id>/update/', views.client_update, name='client_update'),
    path('clients/<int:client_id>/delete/', views.client_delete, name='client_delete'),

    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/update/', views.order_update, name='order_update'),
    path('orders/<int:order_id>/delete/', views.order_delete, name='order_delete'),
]