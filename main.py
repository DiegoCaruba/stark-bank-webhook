import schedule
from scheduler import run_jobs

from app import app
from config import webhook_url
from webhook import setup_webhook
from generate import create_random_invoices


def run():
    """Runs the project"""

    # Ensure webhook is setup
    setup_webhook(webhook_url)

    # Schedule job to create random invoices every 3 hours
    # Warning: doesn't account for lost jobs, program must be running
    # In production, use something like Celery
    schedule.every(3).hours.do(create_random_invoices)

    # Start the scheduler
    stop_run_jobs = run_jobs()

    # Run scheduled jobs for the first time, without having to wait 3 hours
    schedule.run_all()

    # Run the Flask app
    app.run()

    # Stop the scheduler
    stop_run_jobs.set()


if __name__ == "__main__":
    run()
