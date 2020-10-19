from typing import Type

from spark_auto_mapper_fhir.fhir_types.valuesets.administrative_gender import FhirAdministrativeGenderCode
from spark_auto_mapper_fhir.fhir_types.valuesets.marital_status import FhirMaritalStatusCode


class FhirCodeList:
    administrative_gender: Type[FhirAdministrativeGenderCode
                                ] = FhirAdministrativeGenderCode
    """
    The gender of a person used for administrative purposes.
    https://hl7.org/FHIR/valueset-administrative-gender.html
    """
    marital_status: Type[FhirMaritalStatusCode] = FhirMaritalStatusCode
    """
    This value set defines the set of codes that can be used to indicate the marital status of a person
    https://hl7.org/FHIR/valueset-marital-status.html
    """
