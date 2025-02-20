import os
from unittest import mock

import app.config as config

config.private_key = os.path.join(os.path.dirname(__file__), "test_private_key.pem")

from app.services.auth import starkbank
from app.services.logger import logger
from app.services.webhook import setup_webhook


def test_setup_webhook_already_configured():
    """Test that setup_webhook does not create a new webhook when one is already configured."""
    test_url = "https://example.com/webhook"

    # Create a dummy webhook that already matches the criteria.
    dummy_webhook = mock.MagicMock()
    dummy_webhook.url = test_url
    dummy_webhook.subscriptions = ["invoice"]

    with mock.patch.object(
        starkbank.webhook, "query", return_value=[dummy_webhook]
    ), mock.patch.object(logger, "info") as logger_info, mock.patch.object(
        starkbank.webhook, "create"
    ) as create_mock:

        setup_webhook(test_url)

        logger_info.assert_any_call("[+] Webhook is already configured ...")

        create_mock.assert_not_called()


def test_setup_webhook_creates_new():
    """Test that setup_webhook creates a new webhook if none matches the given criteria."""
    test_url = "https://example.com/webhook"

    # Create a dummy webhook that does not match the criteria.
    dummy_webhook = mock.MagicMock()
    dummy_webhook.url = "https://different.com/webhook"
    dummy_webhook.subscriptions = ["invoice"]

    with mock.patch.object(
        starkbank.webhook, "query", return_value=[dummy_webhook]
    ), mock.patch.object(logger, "info") as logger_info, mock.patch.object(
        starkbank.webhook, "create"
    ) as create_mock:

        setup_webhook(test_url)

        expected_log = f"""[*] Creating webhook ...
    URL: {test_url}
    Subscriptions: ["invoice"]\n"""
        logger_info.assert_any_call(expected_log)

        create_mock.assert_called_once_with(url=test_url, subscriptions=["invoice"])
