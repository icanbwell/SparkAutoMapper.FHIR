from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RoleClassServiceDeliveryLocation(GenericTypeCode):
    """
    v3.RoleClassServiceDeliveryLocation
    From: http://terminology.hl7.org/ValueSet/v3-RoleClassServiceDeliveryLocation in v3-codesystems.xml
         A role played by a place at which services may be provided.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-RoleClass
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-RoleClass"


class RoleClassServiceDeliveryLocationValues:
    """
    Corresponds to the Role class
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """

    Role = RoleClassServiceDeliveryLocation("ROL")
    """
    The player of the role is a child of the scoping entity, in a generic sense.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    Child = RoleClassServiceDeliveryLocation("CHILD")
    """
    A role played by an entity that receives credentials from the scoping entity.
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    CredentialedEntity = RoleClassServiceDeliveryLocation("CRED")
    """
    nurse practitioner
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    NursePractitioner = RoleClassServiceDeliveryLocation("NURPRAC")
    """
    nurse
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    Nurse = RoleClassServiceDeliveryLocation("NURS")
    """
    physician assistant
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    PhysicianAssistant = RoleClassServiceDeliveryLocation("PA")
    """
    physician
    From: http://terminology.hl7.org/CodeSystem/v3-RoleClass in v3-codesystems.xml
    """
    Physician = RoleClassServiceDeliveryLocation("PHYS")
