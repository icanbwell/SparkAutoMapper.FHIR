from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CalendarCycle(GenericTypeCode):
    """
    v3.CalendarCycle
    From: http://terminology.hl7.org/ValueSet/v3-CalendarCycle in v3-codesystems.xml
         Calendar cycle identifiers
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-CalendarCycle
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-CalendarCycle"


class CalendarCycleValues:
    """
    CalendarCycleOneLetter
    From: http://terminology.hl7.org/CodeSystem/v3-CalendarCycle in v3-codesystems.xml
    """

    CalendarCycleOneLetter = CalendarCycle("_CalendarCycleOneLetter")
    """
    CalendarCycleTwoLetter
    From: http://terminology.hl7.org/CodeSystem/v3-CalendarCycle in v3-codesystems.xml
    """
    CalendarCycleTwoLetter = CalendarCycle("_CalendarCycleTwoLetter")
    """
    The week with the month's first Thursday in it (analagous to the ISO 8601
    definition for week of the year).
    From: http://terminology.hl7.org/CodeSystem/v3-CalendarCycle in v3-codesystems.xml
    """
    WeekOfTheMonth = CalendarCycle("WM")
