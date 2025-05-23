from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RouteOfAdministration(GenericTypeCode):
    """
    v3.RouteOfAdministration
    From: http://terminology.hl7.org/ValueSet/v3-RouteOfAdministration in v3-codesystems.xml
         The path the administered medication takes to get into the body or into
    contact with the body.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"


class RouteOfAdministrationValues:
    """
    Route of substance administration classified by administration method.
    From: http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration in v3-codesystems.xml
    """

    RouteByMethod = RouteOfAdministration("_RouteByMethod")
    """
    Route of substance administration classified by site.
    From: http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration in v3-codesystems.xml
    """
    RouteBySite = RouteOfAdministration("_RouteBySite")
