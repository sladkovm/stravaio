test: 
	python -m pytest -v

build:
	python setup.py sdist bdist_wheel

