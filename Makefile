LANG=en_US.utf-8

export LANG

Pipfile.lock: Pipfile
	docker compose run --rm --name sam dev sh -c "rm -f Pipfile.lock && pipenv lock --dev"

.PHONY:devdocker
devdocker: ## Builds the docker for dev
	docker compose build

.PHONY:init
init: devdocker up setup-pre-commit  ## Initializes the local developer environment

.PHONY: up
up: Pipfile.lock
	docker compose up --build -d --remove-orphans

.PHONY: down
down:
	docker compose down

.PHONY:clean-pre-commit
clean-pre-commit: ## removes pre-commit hook
	rm -f .git/hooks/pre-commit

.PHONY:setup-pre-commit
setup-pre-commit: Pipfile.lock
	cp ./pre-commit-hook ./.git/hooks/pre-commit

.PHONY:run-pre-commit
run-pre-commit: setup-pre-commit
	./.git/hooks/pre-commit

.PHONY:update
update: down Pipfile.lock setup-pre-commit  ## Updates all the packages using Pipfile
	docker compose run --rm --name spf_pipenv dev pipenv sync --dev && \
	make devdocker && \
	make pipenv-setup

.PHONY:tests
tests: up
	docker compose run --rm --name sam_fhir dev pytest tests

.PHONY:continuous_integration
continuous_integration: run-pre-commit
	docker compose run --rm --name sam_fhir dev python setup.py install && \
    pytest tests

.PHONY: sphinx-html
sphinx-html:
	docker compose run --rm --name sam_fhir dev make -C docsrc html
	@echo "copy html to docs... why? https://github.com/sphinx-doc/sphinx/issues/3382#issuecomment-470772316"
	@rm -rf docs
	@mkdir docs
	@touch docs/.nojekyll
	cp -a docsrc/_build/html/. docs

.PHONY:classes-debug
classes-debug:
	docker compose run --rm --name sam_fhir dev python3 spark_auto_mapper_fhir/generator/generate_classes.py > out.txt

.PHONY:classes
classes:
	docker compose run --rm --name sam_fhir dev python3 spark_auto_mapper_fhir/generator/generate_classes.py && \
	make run-pre-commit

.PHONY:pipenv-setup
pipenv-setup:devdocker ## Run pipenv-setup to update setup.py with latest dependencies
	docker compose run --rm --name spark_pipeline_framework dev sh -c "pipenv run pipenv install --skip-lock --categories \"pipenvsetup\" && pipenv run pipenv-setup sync --pipfile" && \
	make run-pre-commit


.PHONY:shell
shell:devdocker ## Brings up the bash shell in dev docker
	docker compose run --rm --name sam_shell dev /bin/bash

.PHONY:build
build: ## Builds the docker for dev
	docker compose build --progress=plain --parallel
