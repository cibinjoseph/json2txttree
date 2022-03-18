all:
	make dist
	@echo "Now run 'make upload' to upload"

dist:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

upload_test:
	twine upload --repository testpypi dist/*

upload: dist/
	twine upload dist/*

test:
	python3 -m unittest discover

clean:
	rm -rf build json2txttree.egg-info __pycache__ dist
