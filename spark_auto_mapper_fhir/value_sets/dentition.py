from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Dentition(GenericTypeCode):
    """
    v3.Dentition
    From: http://terminology.hl7.org/ValueSet/v3-Dentition in v3-codesystems.xml
        **** MISSING DEFINITIONS ****
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-Dentition
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-Dentition"


class DentitionValues:
    """
    Artificial dentition, artificial subsitutes for the natural dentition
    From: http://terminology.hl7.org/CodeSystem/v3-Dentition in v3-codesystems.xml
    """

    ArtificialDentition = Dentition("ArtificialDentition")
    """
    Permanent dentition, the natural teeth of adulthood that replace or are added
    to the deciduous teeth
    From: http://terminology.hl7.org/CodeSystem/v3-Dentition in v3-codesystems.xml
    """
    PermanentDentition = Dentition("PermanentDentition")
    """
    Primary dentition, the first teeth to errupt and usually replaced with
    permanent dentition
    From: http://terminology.hl7.org/CodeSystem/v3-Dentition in v3-codesystems.xml
    """
    PrimaryDentition = Dentition("PrimaryDentition")
    """
    Supernumerary tooth, any tooth in addition to the normal permanent and primary
    dentition
    From: http://terminology.hl7.org/CodeSystem/v3-Dentition in v3-codesystems.xml
    """
    SupernumeraryTooth = Dentition("SupernumeraryTooth")
