clean: ## Clean
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf html

build: clean ## Build PIPy Package
	python3 setup.py sdist bdist_wheel

check-content: build  ## List contents of PIPy Package
	tar -tvf dist/*.tar.gz

check: build  ## Check PIPy Package
	twine check dist/*

upload: build  ## Upload PIPy Package
	twine upload dist/*

install:  ## Install from repo
	pip3 install -e .

uninstall: ## Uninstall
	pip3 uninstall labml_nn

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: clean build check upload help
.DEFAULT_GOAL := help
