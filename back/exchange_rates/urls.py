from django.urls import path

from . import views

urlpatterns = [
    path("api/v1/today/", views.today_exchange),
]
