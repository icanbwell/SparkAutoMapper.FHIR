from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Systemrestfulinteraction(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class SystemrestfulinteractionValues:
    Transaction = Systemrestfulinteraction("transaction")
    Batch = Systemrestfulinteraction("batch")
    Search_system = Systemrestfulinteraction("search-system")
    History_system = Systemrestfulinteraction("history-system")