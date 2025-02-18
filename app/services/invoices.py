from .auth import starkbank


def generate_invoice(
    tax_id: str, name: str, amount: int, descriptions: list[dict[str, str]] = []
) -> starkbank.Invoice:
    """Generates an invoice with the given data"""
    
    return starkbank.Invoice(
        amount=amount, descriptions=descriptions, tax_id=tax_id, name=name
    )


def create_invoices(invoices: list[starkbank.Invoice]) -> list[starkbank.Invoice]:
    """Creates a list of invoices"""

    returned_invoices = starkbank.invoice.create(invoices)

    for invoice in returned_invoices:
        print(
            f"""[+] Created invoice ...
    ID: #{invoice.id}
    Tax ID: {invoice.tax_id}
    Name: {invoice.name}
    Amount: {invoice.amount}\n"""
        )

    return returned_invoices
