LANG=en_US.utf-8

export LANG

BRANCH=$(shell git rev-parse --abbrev-ref HEAD)
VERSION=$(shell cat VERSION)
VENV_NAME=venv
GIT_HASH=${CIRCLE_SHA1}
SPARK_VER=3.0.1
HADOOP_VER=3.2

include spark_auto_mapper_fhir/Makefile.spark
include spark_auto_mapper_fhir/Makefile.docker
include spark_auto_mapper_fhir/Makefile.python

.PHONY:devsetup
devsetup:venv
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt && \
    pip install --upgrade -r requirements-test.txt && \
    pre-commit install && \
    python setup.py install

.PHONY:checks
checks:venv
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade -r requirements.txt && \
    flake8 spark_auto_mapper_fhir && \
    mypy spark_auto_mapper_fhir && \
    flake8 tests && \
    mypy tests

.PHONY:update
update:
	. $(VENV_NAME)/bin/activate && \
	pip install --upgrade -r requirements.txt && \
	pip install --upgrade -r requirements-test.txt

.PHONY:build
build:venv
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt && \
    python setup.py install && \
    rm -r dist/ && \
    python3 setup.py sdist bdist_wheel

.PHONY:testpackage
testpackage:venv build
	. $(VENV_NAME)/bin/activate && \
	python3 -m twine upload -u __token__ --repository testpypi dist/*
# password can be set in TWINE_PASSWORD. https://twine.readthedocs.io/en/latest/

.PHONY:package
package:venv build
	. $(VENV_NAME)/bin/activate && \
	python3 -m twine upload -u __token__ --repository pypi dist/*
# password can be set in TWINE_PASSWORD. https://twine.readthedocs.io/en/latest/

.PHONY:tests
tests:
	. $(VENV_NAME)/bin/activate && \
    pip install --upgrade -r requirements.txt && \
	pip install --upgrade -r requirements-test.txt && \
	pytest tests

.PHONY:clean-pre-commit
clean-pre-commit:
	pre-commit clean

.PHONY:setup-pre-commit
setup-pre-commit:
	pre-commit install

.PHONY:run-pre-commit
run-pre-commit:
	pre-commit run --all-files

.PHONY:reset-pre-commit
reset-pre-commit: clean-pre-commit run-pre-commit

.PHONY:init
init: installspark up devsetup tests

