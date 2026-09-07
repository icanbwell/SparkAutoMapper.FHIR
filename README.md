[![Build and Test](https://github.com/imranq2/SparkAutoMapper.FHIR/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/imranq2/SparkAutoMapper.FHIR/actions/workflows/build_and_test.yml)

[![Upload Python Package](https://github.com/imranq2/SparkAutoMapper.FHIR/actions/workflows/python-publish.yml/badge.svg)](https://github.com/imranq2/SparkAutoMapper.FHIR/actions/workflows/python-publish.yml)

[![Known Vulnerabilities](https://snyk.io/test/github/imranq2/SparkAutoMapper.FHIR/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/imranq2/SparkAutoMapper.FHIR?targetFile=requirements.txt)

# SparkAutoMapper.FHIR
Add custom FHIR data types to SparkAutoMapper.

## Usage
```shell script
pip install sparkautomapper.fhir
```

## Example
```python
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A
mapper = AutoMapper(
    view="members",
    source_view="patients",
    keys=["member_id"]
).withResource(
    resource=F.patient(
        id_=A.column("a.member_id"),
        birthDate=A.date(
            A.column("date_of_birth")
        ),
        name=A.list(
            F.human_name(
                use="usual",
                family=A.column("last_name")
            )
        ),
        gender="female"
    )
)
```

# Publishing a new package
1. Create a new release
2. The GitHub Action should automatically kick in and publish the package
3. You can see the status in the Actions tab

### Prerequisite: these base-image tags must exist in the services ECR

`helix.spark`'s publish workflows push **only to Docker Hub** — there is no ECR push step —
so the tags below do not reach `856965016623.dkr.ecr.us-east-1.amazonaws.com/helix.spark`
unless someone copies them. Until they do, `docker build` here fails on a missing image.

| tag to copy | expected digest |
|---|---|
| `3.5.5.0-slim` | `sha256:e2c4762e38e3f57bfa99afdd68621c0be46eb373475c5578113c0e683b193126` |

Copy with a manifest-preserving tool. These are multi-arch (`linux/amd64` + `linux/arm64`);
a `docker pull`/`tag`/`push` cycle from an Apple-silicon Mac would push arm64 only and
silently break amd64 CI runners.

```bash
aws sso login --profile services
aws ecr get-login-password --region us-east-1 --profile services \
  | crane auth login 856965016623.dkr.ecr.us-east-1.amazonaws.com --username AWS --password-stdin
DEST=856965016623.dkr.ecr.us-east-1.amazonaws.com/helix.spark
crane copy icanbwell/helix.spark:3.5.5.0-slim "$DEST:3.5.5.0-slim"
# verify:
crane digest "$DEST:3.5.5.0-slim"
```

Source is `icanbwell/helix.spark` (the icanbwell-owned namespace mandated by CIE-8032); it is
digest-identical to the old `imranq2/helix.spark`, so the copy is the same image bytes.

The tag itself is **derived, not chosen**: `A.B.C` in the tag is the Apache Spark version in
the image and must match this repo's `pyspark` pin. Do not change the tag as part of a
registry migration.

See `CIE-8032` for the full decision trail. Copying these tags does NOT by itself make CI
pass — this is a public repo on `ubuntu-latest` with no AWS identity, so a GitHub OIDC
trusted role scoped to `repo:icanbwell/SparkAutoMapper.FHIR:*` is still required.
