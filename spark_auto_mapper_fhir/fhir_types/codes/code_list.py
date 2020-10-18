from typing import Type

from spark_auto_mapper_fhir.fhir_types.codes.administrative_gender import FhirAdministrativeGender


class FhirCodeList:
    administrative_gender: Type[FhirAdministrativeGender] = FhirAdministrativeGender
