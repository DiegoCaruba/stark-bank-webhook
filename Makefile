SHELL := /bin/bash

setup:
	npm i serverless -g
	python3 -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

setup-win:
	npm i serverless -g
	python -m venv .venv
	.venv/Scripts/activate && pip install -r requirements.txt

test:
	source .venv/bin/activate && python3 -m pytest

test-win:
	.venv/Scripts/activate && python -m pytest

deploy:
	source .venv/bin/activate && sls deploy

deploy-win:
	.venv/Scripts/activate && sls deploy

run:
	source .venv/bin/activate && python3 main.py

run-win:
	.venv/Scripts/activate && python main.py

