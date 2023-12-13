from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart),
    path('cartBlank/', views.cartBlank),
    path('product/', views.product),
    path('order/', views.order),
]

