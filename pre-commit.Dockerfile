FROM public.ecr.aws/docker/library/python:3.12-alpine

RUN apk add --no-cache git py3-pip rust cargo && \
    pip install pipenv pre-commit

COPY Pipfile Pipfile.lock ./

RUN pipenv sync --system --dev --verbose

WORKDIR /sourcecode
RUN git config --global --add safe.directory /sourcecode
CMD ["pre-commit", "run", "--all-files"]

# don't default to root.  pre-commit-hook overrides this at runtime with
# --user "$(id -u):$(id -g)" so the bind-mounted /sourcecode stays writable
# whatever UID the host uses.
USER 1001
