.PHONY:  build

REPOSITORY:=testpypi

build: clean install test
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist && rm -rf build && rm -rf take_a_break.egg-info

upload:
	twine check dist/* && twine upload --repository $(REPOSITORY) dist/*

dev:
	pip install --upgrade setuptools wheel twine

install:
	python setup.py develop && pip install .

test:
	pytest