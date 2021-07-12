from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class OMBEthnicityCategory(GenericTypeCode):
    """
    https://www.hl7.org/fhir/us/core/ValueSet-omb-ethnicity-category.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    codeset: FhirUri = "urn:oid:2.16.840.1.113883.6.238"


class OMBEthnicityCategoryValues:
    HispanicOrLatino = OMBEthnicityCategory("2135-2")

    NonHispanicOrLatino = OMBEthnicityCategory("2186-5")
