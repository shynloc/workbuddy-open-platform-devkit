.PHONY: help setup doctor validate schemas records smoke docs source-check source-review

help:
	@echo "WB-OPDK developer commands:"
	@echo "  make setup         Install dev + docs dependencies"
	@echo "  make doctor        Run working-grade local health checks"
	@echo "  make validate      Run KB/source/schema/record validation"
	@echo "  make smoke         Smoke-test starter templates/scaffolds"
	@echo "  make docs          Build HTML knowledge base"
	@echo "  make source-check  Check current official sources"
	@echo "  make source-review Compare official sources with baseline"

setup:
	python3 -m pip install -r requirements-dev.txt
	python3 -m pip install -r requirements-docs.txt

doctor:
	python3 scripts/doctor.py

schemas:
	python3 scripts/validate_schemas.py

records:
	python3 scripts/validate_validation_records.py

validate:
	python3 scripts/validate_kb.py
	python3 scripts/validate_source_registry.py
	python3 scripts/validate_schemas.py
	python3 scripts/validate_validation_records.py

smoke:
	python3 scripts/smoke_test_templates.py

docs:
	python3 scripts/prepare_docs.py
	mkdocs build

source-check:
	python3 scripts/check_official_sources.py

source-review:
	python3 scripts/check_official_sources.py --baseline sources/source-baseline.json