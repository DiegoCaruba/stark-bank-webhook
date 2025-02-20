environment = "sandbox"
project_id = "6311638751772672"
private_key = "privateKey.pem"
webhook_url = "https://v264v4teoa.execute-api.us-east-1.amazonaws.com/dev/webhook"

destination_account = {
    "tax_id": "20.018.183/0001-80",
    "name": "Stark Bank S.A.",
    "bank_code": "20018183",
    "branch_code": "0001",
    "account_number": "6341320293482496",
    "account_type": "payment",
}

# environment = os.getenv("STARKBANK_ENVIRONMENT")
# project_id = os.getenv("SANDBOX_PROJECT_ID")
# private_key = os.getenv("PRIVATE_KEY_PATH")
# webhook_url = os.getenv("WEBHOOK_URL")

# destination_account = {
#     "tax_id": os.getenv("ACCOUNT_TAX_ID"),
#     "name": os.getenv("ACCOUNT_NAME"),
#     "bank_code": os.getenv("ACCOUNT_BANK_CODE"),
#     "branch_code": os.getenv("ACCOUNT_BRANCH_CODE"),
#     "account_number": os.getenv("ACCOUNT_NUMBER"),
#     "account_type": os.getenv("ACCOUNT_TYPE"),
# }
