import os
from dotenv import load_dotenv

load_dotenv()

environment = os.getenv("STARKBANK_ENVIRONMENT")
project_id = os.getenv("SANDBOX_PROJECT_ID")

private_key = os.getenv("PRIVATE_KEY_PATH")

webhook_url = os.getenv("WEBHOOK_URL")

destination_account = {
    "tax_id": os.getenv("ACCOUNT_TAX_ID"),
    "name": os.getenv("ACCOUNT_NAME"),
    "bank_code": os.getenv("ACCOUNT_BANK_CODE"),
    "branch_code": os.getenv("ACCOUNT_BRANCH_CODE"),
    "account_number": os.getenv("ACCOUNT_NUMBER"),
    "account_type": os.getenv("ACCOUNT_TYPE"),
}
