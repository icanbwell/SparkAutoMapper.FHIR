LANG=en_US.utf-8

export LANG

# AWS profile used to reach the services account (856965016623) ECR, which hosts the
# helix.spark base image used by spark.Dockerfile.  Run `aws sso login --profile
# services` first.  pre-commit.Dockerfile stays on public.ecr.aws and needs no
# credentials, so `run-pre-commit` deliberately does NOT depend on this.
AWS_SERVICES_PROFILE ?= services
AWS_SERVICES_REGISTRY = 856965016623.dkr.ecr.us-east-1.amazonaws.com

## Logs docker in to the private ECR that hosts our base images.
## No-op under CI, where the workflow does the login via OIDC role assumption
## (a named local SSO profile does not exist on a GitHub runner).
.PHONY: ecr-login
ecr-login:
	@if [ -n "$$CI" ]; then \
		echo "CI detected - ECR login is handled by the workflow, skipping"; \
	else \
		aws ecr get-login-password --region us-east-1 --profile $(AWS_SERVICES_PROFILE) \
			| docker login --username AWS --password-stdin $(AWS_SERVICES_REGISTRY); \
	fi

Pipfile.lock: Pipfile
	docker compose run --rm --name sam_fhir dev \
		/bin/bash -lc 'pipenv lock --clear --dev'

.PHONY:devdocker
devdocker: ecr-login ## Builds the docker for dev
	docker compose build --no-cache

.PHONY:init
init: devdocker up setup-pre-commit  ## Initializes the local developer environment

.PHONY: up
up: ecr-login Pipfile.lock
	docker compose up --build -d

.PHONY: down
down: ## Brings down all the services in docker-compose
	export DOCKER_CLIENT_TIMEOUT=300 && export COMPOSE_HTTP_TIMEOUT=300
	docker compose down --remove-orphans && \
	docker system prune -f

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
	docker compose run --rm --name sam_fhir_pipenv dev pipenv sync --dev && \
	make pipenv-setup && \
	make devdocker

.PHONY:tests
tests: up
	docker compose run --rm --name sam_fhir_tests dev pytest tests

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
	docker compose run --rm --name sam_fhir dev sh -c "pipenv run pipenv install --skip-lock --categories \"pipenvsetup\" && pipenv run pipenv-setup sync --pipfile" && \
	make run-pre-commit


.PHONY:shell
shell:devdocker ## Brings up the bash shell in dev docker
	docker compose run --rm --name sam_fhir_shell dev /bin/bash

.PHONY:build
build: ecr-login ## Builds the docker for dev
	docker compose build --progress=plain --parallel
