from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Provenanceparticipantrole(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ProvenanceparticipantroleValues:
    Enterer = Provenanceparticipantrole("enterer")
    Performer = Provenanceparticipantrole("performer")
    Author = Provenanceparticipantrole("author")
    Verifier = Provenanceparticipantrole("verifier")
    Attester = Provenanceparticipantrole("attester")
    Informant = Provenanceparticipantrole("informant")
    Custodian = Provenanceparticipantrole("custodian")
    Assembler = Provenanceparticipantrole("assembler")
    Composer = Provenanceparticipantrole("composer")