from random import randint, uniform
from celery import shared_task

from .models import Invoice


@shared_task
def create_invoices():

    for _ in range(randint(8, 12)):
        Invoice.objects.create(
            amount=uniform(10, 1000),
            recipient_name=f"User recipient name: {randint(1, 1000)}"
        )
