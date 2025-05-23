from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContainerMaterialsCode(GenericTypeCode):
    """
    ContainerMaterials
    From: http://hl7.org/fhir/ValueSet/container-material in valuesets.xml
        This value set includes SNOMED CT codes for materials that specimen containers
    are made of
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"


class ContainerMaterialsCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/container-material in valuesets.xml
    """

    Glass = ContainerMaterialsCode("32039001")
    """
    From: http://hl7.org/fhir/ValueSet/container-material in valuesets.xml
    """
    Plastic = ContainerMaterialsCode("61088005")
    """
    From: http://hl7.org/fhir/ValueSet/container-material in valuesets.xml
    """
    Metal = ContainerMaterialsCode("425620007")
