from flask import jsonify, request

from ..app import app
from .auth import starkbank
from .transfer import transfer_from_invoice


def setup_webhook(url: str) -> None:
    """Sets up the webhook for the project"""
    found: bool = False
    webhooks = starkbank.webhook.query()

    for webhook in webhooks:
        if webhook.url == url and "invoice" in webhook.subscriptions:
            print("[+] Webhook is already configured ...")
            found = True
            break

    if not found:
        print(
            f"""[*] Creating webhook ...
    URL: {url}
    Subscriptions: ["invoice"]\n"""
        )
        starkbank.webhook.create(url=url, subscriptions=["invoice"])


@app.route("/webhook", methods=["POST"])
def listen_webhook() -> tuple[str, int]:
    """Listens for webhook events"""

    if not request.is_json:
        return (
            jsonify(
                {
                    "error": "invalid Content-Type, expected application/json",
                    "status_code": 405,
                }
            ),
            405,
        )

    event = starkbank.event.parse(
        content=request.data.decode("utf-8"),
        # Verify the event signature to ensure it was sent by Stark Bank
        signature=request.headers.get("Digital-Signature"),
    )

    print(f"[*] Got event: Subscription: {event.subscription}, Type: {event.log.type}")

    # Handle invoices
    if event.subscription == "invoice":

        # Handle paid invoices
        if event.log.type == "paid":
            transfer_from_invoice(event)

    return jsonify({"status_code": 200, "message": "OK"}), 200
