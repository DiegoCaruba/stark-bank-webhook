import pytest
import starkbank
from unittest.mock import patch, MagicMock

from app.app import app
from app.config import destination_account
from app.services import auth


@pytest.fixture
def test_app():
    """Fixture for the Flask app with a test config."""
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

# Main Fixtures =====================================================
@pytest.fixture
def mock_config():
    """Fixture for mocking the config.py module."""
    with patch("main.webhook_url") as mock_webhook_url:
        mock_webhook_url = "mock_webhook_url"

        # mock_config.environment = "test"
        # mock_config.project_id = "123456"
        # mock_config.private_key = "private_mock_key.pem"
        # mock_config.destination_account = {
        #     "tax_id": "mock_tax_id",
        #     "name": "Test Account",
        #     "bank_code": "mock_bank_code",
        #     "branch_code": "mock_branch_code",
        #     "account_number": "mock_account_number",
        #     "account_type": "mock_account_type",
        # }
        # mock_file = MagicMock()
        # mock_file.read.return_value = "mocked_private_key_content"
        # mock_config.open = MagicMock(return_value=mock_file)

        yield mock_webhook_url


@pytest.fixture
def mock_webhook_setup():
    """Fixture for mocking the setup_webhook module."""

    with patch("app.services.webhook.setup_webhook") as mock_setup_webhook:
        yield mock_setup_webhook


@pytest.fixture
def mock_schedule_and_every():
    """Fixture for mocking the schedule module."""

    with patch("main.schedule.every") as mock_every:
        mock_schedule = MagicMock()
        mock_every.return_value = mock_schedule
        mock_schedule.hours.do.return_value = None

        yield mock_schedule, mock_every


@pytest.fixture
def mock_create_random_invoices():
    """Fixture for mocking the create_random_invoices module."""

    with patch("main.create_random_invoices") as mock_create_random_invoices:
        yield mock_create_random_invoices


@pytest.fixture
def mock_run_jobs():
    """Fixture for mocking the run_jobs module."""

    with patch("main.run_jobs") as mock_run_jobs:
        mock_stop_event = MagicMock()
        mock_run_jobs.return_value = mock_stop_event

        yield mock_run_jobs, mock_stop_event



