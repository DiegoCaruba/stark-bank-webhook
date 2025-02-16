from django.urls import path

from .views import webhook_handler

urlpatterns: list = [
    path("webhook/", webhook_handler, name="webhook")
]
