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
mapper = AutoMapperFhir(
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
