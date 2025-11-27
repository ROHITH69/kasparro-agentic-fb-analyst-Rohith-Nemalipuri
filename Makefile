.PHONY: setup run test

setup:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

run:
	python -m src.run "Analyze why ROAS changed"

test:
	pytest -q
