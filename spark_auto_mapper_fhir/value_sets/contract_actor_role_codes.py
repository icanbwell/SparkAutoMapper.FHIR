from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractActorRoleCodesCode(GenericTypeCode):
    """
    ContractActorRoleCodes
    From: http://terminology.hl7.org/CodeSystem/contractactorrole in valuesets.xml
        This value set includes sample Contract Actor Role codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/contractactorrole
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/contractactorrole"


class ContractActorRoleCodesCodeValues:
    """
    Someone who provides health care related services to people or animals
    including both clinical and support services.
    From: http://terminology.hl7.org/CodeSystem/contractactorrole in valuesets.xml
    """

    Practitioner = ContractActorRoleCodesCode("practitioner")
    """
    A receiver, human or animal, of health care related goods and services.
    From: http://terminology.hl7.org/CodeSystem/contractactorrole in valuesets.xml
    """
    Patient = ContractActorRoleCodesCode("patient")
