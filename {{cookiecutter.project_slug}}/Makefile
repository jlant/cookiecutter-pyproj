.PHONY: clean clean-pyc clean-tests docs tests analysis

define BROWSER_PYTHONSCRIPT
import os
import sys
import webbrowser

try:
    from urllib import pathname2url
except:
    from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYTHONSCRIPT

BROWSER := python -c "$$BROWSER_PYTHONSCRIPT" 

help:
	@echo "make clean: remove all Python artifacts and pytest artifacts"
	@echo "make docs: make Sphinx html documentation"
	@echo "make tests: run tests with pytest"
	@echo "make analysis: run analysis, models, main script, etc."

clean: clean-pyc clean-tests

clean-pyc:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

clean-tests:
	rm -rf .pytest_cache

docs:
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

tests:
	py.test

install: clean
	python setup.py install

analysis:
	@echo "Running analysis:"
	python {{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.py
	@echo ""
