test:
		python -m unittest discover pipeline/tests

open-jupyter:
	./scripts/open_jupyter.sh

.PHONY: open-jupyter
