from app.config import webhook_url
from app.services.webhook import setup_webhook
from app.services.generate import create_random_invoices


def lambda_handler(event, context):
    
    setup_webhook(webhook_url)

    create_random_invoices()
