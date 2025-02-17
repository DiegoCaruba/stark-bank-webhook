from flask import Flask, request
import starkbank
from pycpfcnpj import gen as docgen
import names
import random
import threading
import schedule
import time


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


webhook_url = "https://9f9e-179-101-239-172.ngrok-free.app/webhook"
# webhook_url = "https://db74-2804-7f0-18-9d9-50fe-3875-8c50-8570.ngrok-free.app/webhook"
user = starkbank.Project(
    environment="sandbox",
    id="6311638751772672",
    private_key=open("privateKey.pem").read(),
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
    if obj.get("event", {}).get("subscription") == "invoice":
        if obj.get("event", {}).get("log", {}).get("type") == "paid":
            print(obj.get("event", {}).get("log", {}).get("name", {}))
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

    transfers = starkbank.transfer.create([
        starkbank.Transfer(
            amount=obj.event.log.invoice.amount,
            tax_id="20.018.183/0001-80",
            name="Stark Bank S.A.",
            bank_code="20018183",
            branch_code="0001",
            account_number="6341320293482496",
            account_type="payment"
        )
    ])

    for transfer in transfers:
        print("[+] Transfer completed: ", transfer)





if __name__ == "__main__":
    setup_webhook(webhook_url)
    
    schedule.every(3).hours.do(random_invoices)
    stop_run_jobs = run_jobs()
    # get_invoices()
    app.run()
    stop_run_jobs.set()
    
    