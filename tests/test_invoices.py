import os

import app.config as config

config.private_key = os.path.join(os.path.dirname(__file__), "test_private_key.pem")

from app.services.invoices import generate_invoice


def test_generate_invoice_default_descriptions():
    """
    Test generate_invoice with default descriptions.
    """
    tax_id = "11122233344"
    name = "John Doe"
    amount = 500

    invoice = generate_invoice(tax_id=tax_id, name=name, amount=amount)

    assert invoice.tax_id == tax_id, "tax_id should match the provided tax_id"
    assert invoice.name == name, "name should match the provided name"
    assert invoice.amount == amount, "amount should match the provided amount"

    assert isinstance(invoice.descriptions, list), "Descriptions should be a list"
    assert (
        len(invoice.descriptions) == 0
    ), "Default descriptions should be an empty list"


def test_generate_invoice_with_descriptions():
    """
    Test generate_invoice when descriptions are provided.
    """
    tax_id = "11122233344"
    name = "John Doe"
    amount = 500
    descriptions = [{"item": "Service", "detail": "IT Consulting"}]

    invoice = generate_invoice(
        tax_id=tax_id, name=name, amount=amount, descriptions=descriptions
    )

    assert invoice.tax_id == tax_id, "tax_id should match the provided tax_id"
    assert invoice.name == name, "name should match the provided name"
    assert invoice.amount == amount, "amount should match the provided amount"
    assert (
        invoice.descriptions == descriptions
    ), "Descriptions should match the provided list"
