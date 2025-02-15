from django.urls import path

from .webhook import webhook

urlpatterns: list = [
    path("webhook", webhook, name="webhook")
]