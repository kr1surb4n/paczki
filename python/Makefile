.PHONY: clean virtualenv test document docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

virtualenv:
	virtualenv --prompt '|> codelib <| ' .venv
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source .venv/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=simple \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

check_code:
	pycodestyle ./codelib/*
	pycodestyle ./tests/*

format_code:
	autopep8 -i -r -aaa ./codelib/*
	autopep8 -i -r -aaa ./tests/*

requirements:
	.venv/bin/pip freeze --local > requirements.txt

document:
	pycco -spi -d docs/literate codelib/*

docker: clean
	docker build -t codelib:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
