from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Provenanceparticipanttype(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ProvenanceparticipanttypeValues:
    Enterer = Provenanceparticipanttype("enterer")
    Performer = Provenanceparticipanttype("performer")
    Author = Provenanceparticipanttype("author")
    Verifier = Provenanceparticipanttype("verifier")
    Attester = Provenanceparticipanttype("attester")
    Informant = Provenanceparticipanttype("informant")
    Custodian = Provenanceparticipanttype("custodian")
    Assembler = Provenanceparticipanttype("assembler")
    Composer = Provenanceparticipanttype("composer")