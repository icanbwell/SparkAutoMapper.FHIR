from typing import Type

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.address import AutoMapperFhirDataTypeAddress
from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.coding import AutoMapperFhirDataTypeCoding
from spark_auto_mapper_fhir.fhir_types.human_name import AutoMapperFhirDataTypeHumanName
from spark_auto_mapper_fhir.fhir_types.identifier import AutoMapperFhirDataTypeIdentifier
from spark_auto_mapper_fhir.fhir_types.patient import AutoMapperFhirDataTypePatient
from spark_auto_mapper_fhir.fhir_types.period import AutoMapperFhirDataTypePeriod
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference


class AutoMapperFhirHelpers:
    patient: Type[AutoMapperFhirDataTypePatient] = AutoMapperFhirDataTypePatient
    human_name: Type[AutoMapperFhirDataTypeHumanName] = AutoMapperFhirDataTypeHumanName
    address: Type[AutoMapperFhirDataTypeAddress] = AutoMapperFhirDataTypeAddress
    # noinspection SpellCheckingInspection
    codeableConcept: Type[AutoMapperFhirDataTypeCodeableConcept] = AutoMapperFhirDataTypeCodeableConcept
    coding: Type[AutoMapperFhirDataTypeCoding] = AutoMapperFhirDataTypeCoding
    identifier: Type[AutoMapperFhirDataTypeIdentifier] = AutoMapperFhirDataTypeIdentifier
    period: Type[AutoMapperFhirDataTypePeriod] = AutoMapperFhirDataTypePeriod
    reference: Type[AutoMapperFhirDataTypeReference] = AutoMapperFhirDataTypeReference

    @classmethod
    def code(cls, value: AutoMapperTextInputType) -> AutoMapperFhirCodeInputType:
        return value
