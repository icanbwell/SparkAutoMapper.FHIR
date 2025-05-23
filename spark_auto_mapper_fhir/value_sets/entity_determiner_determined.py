from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EntityDeterminerDetermined(GenericTypeCode):
    """
    v3.EntityDeterminerDetermined
    From: http://terminology.hl7.org/ValueSet/v3-EntityDeterminerDetermined in v3-codesystems.xml
         The described determiner is used to indicate that the given Entity is taken
    as a general description of a kind of thing that can be taken in whole, in
    part, or in multiples.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-EntityDeterminer
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-EntityDeterminer"


class EntityDeterminerDeterminedValues:
    """
    Description:A determiner that specifies that the Entity object represents a
    particular physical thing (as opposed to a universal, kind, or class of
    physical thing).


                               Discussion: It does not matter whether an INSTANCE
    still exists as a whole at the point in time (or process) when we mention it,
    for example, a drug product lot is an INSTANCE even though it has been
    portioned out for retail purpose.
    From: http://terminology.hl7.org/CodeSystem/v3-EntityDeterminer in v3-codesystems.xml
    """

    Specific = EntityDeterminerDetermined("INSTANCE")
    """
    Description:A determiner that specifies that the Entity object represents a
    universal, kind or class of physical thing (as opposed to a particular thing).
    From: http://terminology.hl7.org/CodeSystem/v3-EntityDeterminer in v3-codesystems.xml
    """
    Described = EntityDeterminerDetermined("KIND")
