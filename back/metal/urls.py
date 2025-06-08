from django.urls import path
from . import views

urlpatterns = [
    path('<str:metal_type>/', views.metal_price_chart),
]
