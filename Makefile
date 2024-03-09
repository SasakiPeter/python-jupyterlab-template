test:
		python -m unittest discover src/tests

open-jupyter:
	./scripts/open_jupyter.sh

.PHONY: open-jupyter
