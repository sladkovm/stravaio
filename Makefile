test: 
	python -m pytest -v

build:
	python setup.py sdist bdist_wheel

test_upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*

