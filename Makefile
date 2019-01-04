test: 
	python -m pytest -v

clean:
	python setup.py clean

bbuild:
	python setup.py bbuild

test_upload:
	python setup.py test_upload
	# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	python setup.py upload
	# twine upload dist/*

release:
	git push origin --tags