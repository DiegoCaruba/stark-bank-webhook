import names
import random
from pycpfcnpj import gen as docgen

from app.services.auth import starkbank
from app.services.logger import logger
from app.services.invoices import create_invoices, generate_invoice


def generate_random_invoice() -> starkbank.Invoice:
    """Generates an invoice with random data"""
    return generate_invoice(
        tax_id=docgen.cpf(),
        name=names.get_full_name(),
        amount=random.randint(1, 10000),
    )


def create_random_invoices(
    min_count: int = 8, max_count: int = 12
) -> list[starkbank.Invoice]:
    """Creates between min_count and max_count random invoices"""

    logger.info("[*] Generating random invoices...")
    invoices = []

    for _ in range(random.randint(min_count, max_count)):
        invoice = generate_random_invoice()
        invoices.append(invoice)
        break
    
    return create_invoices(invoices)
