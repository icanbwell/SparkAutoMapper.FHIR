from typing import Type

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.valuesets.code_list import FhirCodeList
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod


class AutoMapperFhirHelpers:
    patient: Type[FhirPatient] = FhirPatient
    human_name: Type[FhirHumanName] = FhirHumanName
    address: Type[FhirAddress] = FhirAddress
    identifier: Type[FhirIdentifier] = FhirIdentifier
    period: Type[FhirPeriod] = FhirPeriod
    codes: Type[FhirCodeList] = FhirCodeList
