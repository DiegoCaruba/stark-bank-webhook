import pytest
from unittest.mock import patch

from main import run


@patch("app.config.webhook_url")
@patch("app.services.webhook.setup_webhook")
# @patch("main.create_random_invoices")
def test_run_function(mock_webhook_setup, mock_webhook_url, mock_create_random_invoices, mock_schedule_and_every):
    mock_schedule, mock_every = mock_schedule_and_every
    
    run()
    
    mock_webhook_setup.assert_called_once_with(mock_webhook_url)
    # mock_every.assert_called_once_with(3)
    # mock_schedule.hours.do.assert_called_once_with(mock_create_random_invoices)
    