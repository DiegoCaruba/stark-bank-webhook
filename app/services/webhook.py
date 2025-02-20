from flask import jsonify, request

from app.app import app
from app.services.logger import logger
from app.services.auth import starkbank
from app.services.transfer import transfer_from_invoice


def setup_webhook(url: str) -> None:
    """Sets up the webhook for the project"""
    found: bool = False
    webhooks = starkbank.webhook.query()

    for webhook in webhooks:
        if webhook.url == url and "invoice" in webhook.subscriptions:
            logger.info("[+] Webhook is already configured ...")
            found = True
            break

    if not found:
        logger.info(
            f"""[*] Creating webhook ...
    URL: {url}
    Subscriptions: ["invoice"]\n"""
        )
        starkbank.webhook.create(url=url, subscriptions=["invoice"])


def handle_event(event):
    # Handle invoices
    if event.subscription == "invoice":

        # Handle paid invoices
        if event.log.type == "paid":
            transfer_from_invoice(event)


def parse_event(content, signature):
    return starkbank.event.parse(
        content=content,
        # Verify the event signature to ensure it was sent by Stark Bank
        signature=signature,
    )


@app.route("/webhook", methods=["POST"])
def listen_webhook() -> tuple[str, int]:
    """Listens for webhook events"""

    if not request.is_json:
        return (
            jsonify(
                {
                    "error": "invalid Content-Type, expected application/json",
                    "status_code": 415,
                }
            ),
            415,
        )

    event = parse_event(request.data.decode("utf-8"), request.headers.get("Digital-Signature"))

    logger.info(f"[*] Got event: Subscription: {event.subscription}, Type: {event.log.type}")

    handle_event(event)

    return jsonify({"status_code": 200, "message": "OK"}), 200
