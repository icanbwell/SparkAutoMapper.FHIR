from typing import Type

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.codes.code_list import FhirCodeList
from spark_auto_mapper_fhir.fhir_types.coding import FhirCoding
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class AutoMapperFhirHelpers:
    patient: Type[FhirPatient] = FhirPatient
    human_name: Type[FhirHumanName] = FhirHumanName
    address: Type[FhirAddress] = FhirAddress
    # noinspection SpellCheckingInspection
    codeableConcept: Type[FhirCodeableConcept] = FhirCodeableConcept
    coding: Type[FhirCoding] = FhirCoding
    identifier: Type[FhirIdentifier] = FhirIdentifier
    period: Type[FhirPeriod] = FhirPeriod
    reference: Type[FhirReference] = FhirReference
    codes: Type[FhirCodeList] = FhirCodeList
