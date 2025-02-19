from app.services.generate import create_random_invoices

def lambda_handler(event, context):
    create_random_invoices()

