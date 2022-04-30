.PHONY: help clean clean-build clean-pyc clean-test coverage check_code dist dist-upload docs document docker format_code install lint requirements servedocs test test-all virtualenv

dm-runserver:
	python manage.py runserver

dm-test:
	python manage.py test $(TEST)

dm-migrate:
	python manage.py migrate

dm-makemigrations:
	python manage.py makemigrations $(APP)

dm-startapp:
	python manage.py startapp $(APP)

dm-startproject:
	django-admin startproject $(PROJECT)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

coverage: ## check code coverage quickly with the default Python
	coverage run --source paczekfiller -m pytest
	coverage report -m

check_code:
	pycodestyle $(APP)

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/paczekfiller.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ paczekfiller
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

document:
	pycco -spi -d docs/literate happy_repo/*

docker: clean
	docker build -t happy_repo:latest .

format_code:
	autopep8 -i -r -aaa ./happy_repo/*
	autopep8 -i -r -aaa ./tests/*

install: clean ## install the package to the active Python's site-packages
	python setup.py install

lint: ## check style with flake8
	flake8 paczekfiller tests

requirements:
	.venv/bin/pip freeze --local > requirements.txt

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

set-origin:
	git remote add git@localhost:$(NAME).git

set-heaven:
	git remote add git@whereibend.space:/repository/$(NAME).git

test:
	python -m pytest \
		-v \
		--cov=simple \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

test-all: ## run tests on every Python version with tox
	tox
