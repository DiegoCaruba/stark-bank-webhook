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
  make setup     # For Unix-based systems
  make setup-win # For Windows
  ```

## Usage

### Environment Configuration
1. It is necessary be have access to STARK BANK API
2. Create a project and fetch 'ID do projeto'
3. Obtain a public and private key at STARK BANK API
4. Set app/config.py
  - The project_id variable must receive 'ID do projeto'
  - Allocate your privateKey.pem file and set private_key variable with file path
  - Set webhook_url with a valid URL

#### Running Local Mode:
  - It may be necessary to use a tool that creates secure tunnels from the internet to your local machine, such as Ngrok
  - The public URL must be replace webhook_url value at app/config.py

#### Running AWS with Serverless Framework
  - The first time you run Serverless, it will be given an AWS URL
  - Set webhook_url with this URL and run the deploy command again

### Local Mode

Start the application with the following:
```bash
make run     # For Unix-based systems
make run-win # For Windows
```

This starts a Flask server and the local scheduler will trigger invoice generation every 3 hours (with an immediate run at start).

### AWS Deployment

Deploy the application to AWS using the Serverless Framework:

```bash
make deploy     # For Unix-based systems
make deploy-win # For Windows
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
- It is necessary to create 'tests/test_private_key.pem' file with a valid private-key to run all tests suites

```bash
make test     # For Unix-based systems
make test-win # For Windows
```

This will execute unit tests for invoice generation, invoice creation, and webhook setup.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
