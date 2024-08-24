from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-service/', views.add_service, name='add-service'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('add-service-to-cart/', views.add_services_to_cart, name='add-service-to-cart'),
    path('delete-service-from-cart/<int:pk>/', views.delete_service_from_cart, name='delete-service-from-cart'),
    path('check-out-here/', views.checkout_here, name='checkout-here'),
    path('pay-for-laundry/', views.pay_for_laundry, name='pay-for-laundry'),
    path('completed-payment/', views.completed_payment, name='completed-payment'),
    path('services/', views.services, name='services'),
    path('add-product/', views.add_product, name='add-product'),
    path('products/', views.product_list, name='product-list'),
    path('mark-complete/<int:id>/', views.mark_complete, name='mark_complete'),
    path('mark-delivered/<int:id>/', views.mark_delivered, name='mark_delivered'),
    path('order-history/', views.order_history, name='order_history')

    
]
