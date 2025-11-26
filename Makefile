PYTHON ?= python

.PHONY: install run test format lint
install:
	$(PYTHON) -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt
run:
	@[ -n "$$QUERY" ] || (echo "Usage: make run QUERY='Analyze ROAS drop'"; exit 1)
	$(PYTHON) src/run.py "$(QUERY)"
test:
	$(PYTHON) -m pytest -q
