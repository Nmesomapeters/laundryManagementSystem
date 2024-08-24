from django.urls import path
from .views import register_admin, custom_admin_login, logout_admin

urlpatterns = [
    # Admin authentication
    path('admin-register/', register_admin, name='admin_register'),
    path('admin-login/', custom_admin_login, name='admin_login'),
    path('admin-logout/', logout_admin, name='admin_logout'),
]