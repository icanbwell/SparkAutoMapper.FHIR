FROM public.ecr.aws/docker/library/python:3.12-alpine
# Set by CIE-5665.  This clears CUSTOM-RULE-559 (unapproved registry) but NOT
# CUSTOM-RULE-2300, which accepts only .../root-mirror/*.  2300 is knowingly left open
# here; it is tracked as an Aikido rule-exception request rather than a code change.
#
# The one-line flip that WOULD clear 2300, recorded for whoever picks that up later:
#   FROM 856965016623.dkr.ecr.us-east-1.amazonaws.com/root-mirror/python:3.12-alpine3.22
# Confirmed with aikido_full_scan (2026-09-08) to clear both 559 and 2300. NOT adopted,
# deliberately:
#   - that tag's existence in the mirror is unverified (no AWS credentials available),
#     and an org-wide search found no other repo using it;
#   - every working root-mirror precedent in the org (fhir_to_llm,
#     patient-intake-service, helix.providersearch) is a PRIVATE repo on a self-hosted
#     `runs-on: main` runner, one relying on ambient IRSA. This repo is PUBLIC on
#     ubuntu-latest and cannot use any of those auth paths;
#   - keeping public.ecr.aws means pre-commit needs no registry credentials at all, so
#     `make run-pre-commit` still works for forks and outside contributors.
# If adopting it, first mirror the tag via icanbwell/aikido-image-sync
# (POST /request then /mirror with {"image":"python:3.12-alpine3.22"}).

RUN apk add --no-cache git py3-pip rust cargo && \
    pip install pipenv pre-commit

COPY Pipfile Pipfile.lock ./

RUN pipenv sync --system --dev --verbose

WORKDIR /sourcecode
# --system (i.e. /etc/gitconfig) rather than --global: this build stage runs as root,
# so --global would land in /root/.gitconfig, which the non-root runtime user cannot
# read - especially since pre-commit-hook also sets HOME=/tmp.
RUN git config --system --add safe.directory /sourcecode
CMD ["pre-commit", "run", "--all-files"]

# Don't default to root (CKV_DOCKER_3).  A real named user is created rather than a
# bare numeric UID so HOME/shell lookups resolve.  pre-commit-hook still overrides
# this at runtime with --user "$(id -u):$(id -g)" -e HOME=/tmp, which is REQUIRED:
# pre-commit's formatters rewrite files in the bind-mounted /sourcecode, so the
# container user has to match the host UID that owns the checkout.
RUN addgroup -g 1000 precommit && adduser -u 1000 -G precommit -s /bin/sh -D precommit
USER precommit
