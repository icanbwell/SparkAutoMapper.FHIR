from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PostalAddressUse(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class PostalAddressUseValues:
    _generaladdressuse = PostalAddressUse("_GeneralAddressUse")
    _postaladdressuse = PostalAddressUse("_PostalAddressUse")
    _telecommunicationaddressuse = PostalAddressUse("_TelecommunicationAddressUse")
    BadAddress = PostalAddressUse("BAD")
    ConfidentialAddress = PostalAddressUse("CONF")
    PrimaryHome = PostalAddressUse("HP")
    VacationHome = PostalAddressUse("HV")
    Direct = PostalAddressUse("DIR")
    Public = PostalAddressUse("PUB")
    PhysicalVisitAddress = PostalAddressUse("PHYS")
    PostalAddress = PostalAddressUse("PST")