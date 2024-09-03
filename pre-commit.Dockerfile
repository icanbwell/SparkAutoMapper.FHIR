FROM public.ecr.aws/docker/library/python:3.12-alpine

RUN apk add --no-cache git py3-pip rust cargo && \
    pip install pipenv pre-commit

COPY Pipfile* ./

RUN pipenv sync --dev --system --extra-pip-args="--prefer-binary"

WORKDIR /sourcecode
RUN git config --global --add safe.directory /sourcecode
CMD ["pre-commit", "run", "--all-files"]
