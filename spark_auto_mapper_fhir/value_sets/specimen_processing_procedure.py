from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SpecimenProcessingProcedureCode(GenericTypeCode):
    """
    SpecimenProcessingProcedure
    From: http://hl7.org/fhir/ValueSet/specimen-processing-procedure in valuesets.xml
        The technique that is used to perform the process or preserve the specimen.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v2-0373
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v2-0373"


class SpecimenProcessingProcedureCodeValues:
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """

    Acidification = SpecimenProcessingProcedureCode("ACID")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """
    Alkalization = SpecimenProcessingProcedureCode("ALK")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """
    Defibrination = SpecimenProcessingProcedureCode("DEFB")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """
    Filtration = SpecimenProcessingProcedureCode("FILT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """
    LDLPrecipitation = SpecimenProcessingProcedureCode("LDLP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """
    Neutralization = SpecimenProcessingProcedureCode("NEUT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """
    Recalification = SpecimenProcessingProcedureCode("RECA")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0373 in v2-tables.xml
    """
    Ultrafiltration = SpecimenProcessingProcedureCode("UFIL")
