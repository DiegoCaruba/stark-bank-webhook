from flask import Flask, request
import starkbank
from pycpfcnpj import gen as docgen
import names
import random
import threading
import schedule
import time
import os
from dotenv import load_dotenv
load_dotenv()


def run_jobs(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


webhook_url = os.getenv("WEBHOOK_URL")

user = starkbank.Project(
    environment=os.getenv("STARKBANK_ENVIRONMENT"),
    id=os.getenv("SANDBOX_PROJECT_ID"),
    private_key=open(os.getenv("PRIVATE_KEY_PATH")).read(),
)
starkbank.user = user


app = Flask(__name__)


def setup_webhook(url: str):
    found: bool = False    
    webhooks = starkbank.webhook.query()

    for webhook in webhooks:
        if webhook.url == webhook_url and "invoice" in webhook.subscriptions:
            print("[+] Webhook is already configured")
            found = True
            break
    
    if not found:
        print("[*] Creating webhook...")
        starkbank.webhook.create(
            url=webhook_url,
            subscriptions=["invoice"]
        )

@app.route("/")
def hello():
    return "Olá"


@app.route("/webhook", methods=["POST"])
def listen_webhook():

    if request.headers.get("Content-Type") != "application/json":
        return "", 405

    obj = request.json
    # print(f"{obj=}")
    if obj.get("event", {}).get("subscription") == "invoice":
        if obj.get("event", {}).get("log", {}).get("type") == "paid":
            # print(obj.get("event", {}).get("log", {}).get("name", {}))
            transfer_invoice(obj)
            
    return "OK"


# AGENDA a cada 3 horas e TRANSFER
# 

def generate_invoice(tax_id, name, amount, descriptions=None):  
    return starkbank.Invoice(amount=amount, descriptions=descriptions, tax_id=tax_id, name=name )


def create_invoices(invoices):  
    returned_invoices = starkbank.invoice.create(invoices)
    
    for invoice in returned_invoices:
        print("[+] Created invoice: ", invoice)


def random_invoices():
    invoices = []

    for i in range(random.randint(8, 12)):
        invoices.append(generate_invoice(
            tax_id=docgen.cpf(),
            name=names.get_full_name(),
            amount=random.randint(1, 10000)
        ))
        break
    
    create_invoices(invoices=invoices)


def get_invoices():
    invoices = starkbank.invoice.query(
        after="2025-02-16",
        before="2025-02-17",
        # status="created"
        status="paid"
    )

    for invoice in invoices:
        print(invoice.tax_id, invoice.status)


def transfer_invoice(obj):
    print(f"Transfer = {obj}")
    # transfers = starkbank.transfer.create([
    #     starkbank.Transfer(
    #         amount = obj.event.log.invoice.amount,
    #         tax_id = os.getenv("ACCOUNT_TAX_ID")",
    #         name = os.getenv("ACCOUNT_NAME"),
    #         bank_code = os.getenv("ACCOUNT_BANK_CODE"),
    #         branch_code = os.getenv("ACCOUNT_BRANCH_CODE"),
    #         account_number =  os.getenv("ACCOUNT_NUMBER"),
    #         account_type = os.getenv("ACCOUNT_TYPE")
    #     )
    # ])

    # for transfer in transfers:
        # print("[+] Transfer completed: ", transfer)





if __name__ == "__main__":
    setup_webhook(webhook_url)
    
    # schedule.every(3).hours.do(random_invoices)
    # stop_run_jobs = run_jobs()
    random_invoices()
    # get_invoices()
    app.run()
    # stop_run_jobs.set()
    
    