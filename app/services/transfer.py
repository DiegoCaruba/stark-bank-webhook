from .auth import starkbank
from ..config import destination_account


def transfer_from_invoice(event: starkbank.Event) -> list[starkbank.Transfer]:
    """Transfers the amount from the invoice to the destination account"""

    invoice = event.log.invoice

    transfer = starkbank.Transfer(
        amount=invoice.amount - invoice.fee,
        description=f"Transfer from invoice #{invoice.id}",
        **destination_account,
    )

    transfers = starkbank.transfer.create([transfer])

    for transfer in transfers:
        print(
            f"""[+] Transfer created ...
    ID: #{transfer.id}
    Invoice ID: #{invoice.id}
    Destination Tax ID: {transfer.tax_id}
    Destination Name: {transfer.name}
    Destination Bank Code: {transfer.bank_code}
    Destination Branch Code: {transfer.branch_code}
    Amount: {transfer.amount}\n"""
        )

    return transfers
