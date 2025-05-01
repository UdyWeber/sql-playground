.PHONY: rm-dbg run

run:
	python src/main.py

rm-dbg:
	@find . -type f -name "*.py" -exec sed -i '/^[[:space:]]*breakpoint()[[:space:]]*$$/d' {} +
