from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Listemptyreasons(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ListemptyreasonsValues:
    NilKnown = Listemptyreasons("nilknown")
    NotAsked = Listemptyreasons("notasked")
    InformationWithheld = Listemptyreasons("withheld")
    Unavailable = Listemptyreasons("unavailable")
    NotStarted = Listemptyreasons("notstarted")
    Closed = Listemptyreasons("closed")