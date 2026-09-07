FROM 856965016623.dkr.ecr.us-east-1.amazonaws.com/helix.spark:3.5.5.0-slim
# https://github.com/icanbwell/helix.spark
# Pulled from the services-account private ECR per CIE-8032 (the icanbwell/helix.spark
# Docker Hub repo is now private).  The 3.5.5.0 tag is dictated by the pyspark==3.5.5
# pin in Pipfile - the Python and JVM halves of Spark must match - so do NOT change the
# tag here without changing that pin.  Requires `make ecr-login` locally.
USER root

ENV PYTHONPATH=/sam_fhir
ENV CLASSPATH=/sam_fhir/jars:$CLASSPATH

COPY Pipfile Pipfile.lock  /sam_fhir/
WORKDIR /sam_fhir

RUN df -h # for space monitoring
RUN pipenv sync --system --dev --extra-pip-args="--prefer-binary"

# override entrypoint to remove extra logging
RUN mv /opt/minimal_entrypoint.sh /opt/entrypoint.sh

COPY . /sam_fhir

# run pre-commit once so it installs all the hooks and subsequent runs are fast
# RUN pre-commit install
RUN df -h # for space monitoring
RUN mkdir -p /fhir && chmod 777 /fhir
RUN mkdir -p /.local/share/virtualenvs && chmod 777 /.local/share/virtualenvs
# USER 1001

# Run as non-root user
# Change ownership of the directory and its subdirectories
RUN chown -R 185:185 /sam_fhir

# Set permissions to allow writing (read, write, execute for owner)
RUN chmod -R 755 /sam_fhir
# https://spark.apache.org/docs/latest/running-on-kubernetes.html#user-identity
USER 185
