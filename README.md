# StarkBank Webhook & Invoice Automation

This repository provides a simple serverless application to integrate with Stark Bank. It supports automated invoice generation with random data and webhook handling.

The application can be run locally using a built-in scheduler or deployed on AWS Lambda with scheduled events.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [License](#license)

## Overview

This project handles:

- Generating random invoices with realistic data (random names, CPF tax IDs, and amounts)
- Creating invoices on Stark Bank’s platform
- Setting up webhooks to handle invoice events
- Transferring funds for paid invoices

## Architecture

The project consists of:

- **AWS Lambda & Serverless Framework:** The `serverless.yml` file deploys main Lambda functions:
  - A webhook listener handling POST requests.
  - A scheduled function for generating random invoices.
- **Flask Application:** A lightweight Flask app (`app.py`) handles HTTP webhook events.
- **Local Scheduler:** When using `make run` locally, a scheduler sets up invoice generation every 3 hours.
- **Stark Bank Integration:** Uses the Stark Bank SDK for invoice and transfer operations.

## Features

- **Simple Serverless Setup:** Easily deploy the application via AWS Lambda.
- **Webhook Handling:** Process invoice events with basic verification.
- **Invoice Generation:** Create invoices with randomly generated data.
- **Dual Execution Mode:**
  - **Local:** Run with `make run` (includes a local scheduler).
  - **AWS:** Deploy via `make deploy` where AWS CloudWatch triggers scheduled jobs.
- **Basic Testing:** Unit tests using pytest to verify functionality.

## Requirements

- Python 3.12
- AWS Account with Lambda permissions (for deployment)
- Node.js (for installing the Serverless CLI)
- Required Python dependencies (see `requirements.txt`)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/DiegoCaruba/stark-bank-webhook.git
   cd stark-bank-webhook
   ```

2. **Install Serverless CLI and Python dependencies:**

   ```bash
   make setup
   ```

## Usage

### Local Mode

For local testing and development, run:

```bash
make run
```

This starts a Flask server and the local scheduler will trigger invoice generation every 3 hours (with an immediate run at start).

### AWS Deployment

Deploy the application to AWS using the Serverless Framework:

```bash
make deploy
```

AWS CloudWatch events replace the local scheduler for triggering the scheduled function.

## Project Structure

```
.
├── app
│   ├── app.py                     # Flask application entry point
│   ├── config.py                  # Configuration settings
│   ├── services
│   │   ├── auth.py                # Stark Bank authentication
│   │   ├── generate.py            # Random invoice generation
│   │   ├── invoices.py            # Invoice creation and management
│   │   ├── logger.py              # Logging setup
│   │   ├── scheduler.py           # Local scheduler for development
│   │   ├── transfer.py            # Handling transfers from invoices
│   │   └── webhook.py             # Webhook listener and event processing
│   └── lambda.py                  # AWS Lambda handler for scheduled invoice generation
├── main.py                        # Entry point for local execution (includes scheduler)
├── Makefile                       # Commands for setup, testing, and deployment
├── serverless.yml                 # Serverless Framework configuration for AWS deployment
└── tests
    ├── test_generate.py           # Unit tests for random invoice generation
    ├── test_invoices.py           # Unit tests for invoice creation
    └── test_webhook.py            # Unit tests for webhook handling
```

## Testing

Run the test suite with:

```bash
make test
```

This will execute unit tests for invoice generation, invoice creation, and webhook setup.

## Deployment

Deploy the application to AWS with:

```bash
make deploy
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
