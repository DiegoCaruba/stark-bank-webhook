import os

import app.config as config

config.private_key = os.path.join(os.path.dirname(__file__), "test_private_key.pem")

from app.services.generate import generate_random_invoice


def test_generate_random_invoice():
    """Test basic properties of a randomly generated invoice."""
    invoice = generate_random_invoice()

    assert hasattr(invoice, "tax_id"), "Invoice should have a tax_id attribute"
    assert hasattr(invoice, "name"), "Invoice should have a name attribute"
    assert hasattr(invoice, "amount"), "Invoice should have an amount attribute"

    assert (
        isinstance(invoice.name, str) and invoice.name
    ), "Invoice name should be a non-empty string"
    assert (
        isinstance(invoice.tax_id, str) and invoice.tax_id
    ), "Invoice tax_id should be a non-empty string"
    assert (
        isinstance(invoice.amount, int) and 1 <= invoice.amount <= 10000
    ), "Invoice amount should be between 1 and 10000"
