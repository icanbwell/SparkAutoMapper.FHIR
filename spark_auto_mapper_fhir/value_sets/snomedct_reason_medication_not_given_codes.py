from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SNOMEDCTReasonMedicationNotGivenCodesCode(GenericTypeCode):
    """
    SNOMEDCTReasonMedicationNotGivenCodes
    From: http://hl7.org/fhir/reason-medication-not-given in valuesets.xml
        This value set includes all medication refused, medication not administered,
    and non-administration of necessary drug or medicine codes from SNOMED CT -
    provided as an exemplar value set.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/reason-medication-not-given
    """
    codeset: FhirUri = "http://hl7.org/fhir/reason-medication-not-given"


class SNOMEDCTReasonMedicationNotGivenCodesCodeValues:
    """
    No reason known.
    From: http://hl7.org/fhir/reason-medication-not-given in valuesets.xml
    """

    None_ = SNOMEDCTReasonMedicationNotGivenCodesCode("a")
    """
    The patient was not available when the dose was scheduled.
    From: http://hl7.org/fhir/reason-medication-not-given in valuesets.xml
    """
    Away = SNOMEDCTReasonMedicationNotGivenCodesCode("b")
    """
    The patient was asleep when the dose was scheduled.
    From: http://hl7.org/fhir/reason-medication-not-given in valuesets.xml
    """
    Asleep = SNOMEDCTReasonMedicationNotGivenCodesCode("c")
    """
    The patient was given the medication and immediately vomited it back.
    From: http://hl7.org/fhir/reason-medication-not-given in valuesets.xml
    """
    Vomit = SNOMEDCTReasonMedicationNotGivenCodesCode("d")
