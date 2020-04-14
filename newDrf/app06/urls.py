from django.contrib import admin
from django.urls import path, include

from .views import Cars, LoginView, Service

urlpatterns = [
    path('carts/', Cars.as_view(), name='carts'),
    path('login_view', LoginView.as_view(), name='login'),
    path('<str:version>/version/', Service.as_view(), name='version')
]
