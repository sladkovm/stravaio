test: 
	python -m pytest -v

clean:
	python setup.py clean

bbuild:
	python setup.py clean
	python setup.py bbuild

test_upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*

release:
	git push origin --tags