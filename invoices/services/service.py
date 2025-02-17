from starkbank import user
from starkbank import transfer


user = starkbank.Project(
    environment="sandbox",
    id="5656565656565656",
    private_key=private_key_content
)


def transfer_amount(amount: float) -> None:
    user.project = "id"

    transfer_data: dict = {
        "amount": amount,
        "bank_code": "20018183",
        "branch_code": "0001",
        "account_number": "6341320293482496",
        "tax_id": "20.018.183/0001-80",
        "name": "Stark Bank S.A."  
    }

    transfer.create(**transfer_data)
