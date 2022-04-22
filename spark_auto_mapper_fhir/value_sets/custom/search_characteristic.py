from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class SearchCharacteristicCode(GenericTypeCode):
    """
    Custom codeset for providerSearch.searchCharacteristic extension
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    codeset: FhirUri = "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/ValueSet/search_characteristic"


class SearchCharacteristicCodeValues:
    """
    Resource populateS in front-end search results
    """

    Searchable = SearchCharacteristicCode("searchable")

    """
    Resource is available for appointment creations
    """
    Bookable = SearchCharacteristicCode("bookable")

    """
    Resource is available for appointment creations
    """
    BookablePhone = SearchCharacteristicCode("bookable-phone")

    """
    Resource is available for appointment creations
    """
    BookableOnline = SearchCharacteristicCode("bookable-online")

    """
    Resource is available for appointment creations
    """
    NotBookable = SearchCharacteristicCode("not-bookable")

    """
    Resource is available for appointment creations
    """
    NotSearchable = SearchCharacteristicCode("hide-from-search")
