from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProvenanceParticipantType(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ProvenanceParticipantTypeValues:
    Enterer = ProvenanceParticipantType("enterer")
    Performer = ProvenanceParticipantType("performer")
    Author = ProvenanceParticipantType("author")
    Verifier = ProvenanceParticipantType("verifier")
    Attester = ProvenanceParticipantType("attester")
    Informant = ProvenanceParticipantType("informant")
    Custodian = ProvenanceParticipantType("custodian")
    Assembler = ProvenanceParticipantType("assembler")
    Composer = ProvenanceParticipantType("composer")