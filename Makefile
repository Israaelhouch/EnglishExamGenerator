SHELL := /bin/bash
VENV := env
ACTIVATE := source $(VENV)/bin/activate

.PHONY: venv install run clean

venv:
	python3 -m venv $(VENV)

install: venv
	$(ACTIVATE) && pip install --upgrade pip && pip install -r backend/requirements.txt

run: 
	$(ACTIVATE) && uvicorn main:app --host 0.0.0.0 --port 8080 --reload


clean:
	rm -rf $(VENV)
