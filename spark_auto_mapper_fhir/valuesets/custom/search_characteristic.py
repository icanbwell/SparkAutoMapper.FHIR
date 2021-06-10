from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SearchCharacteristicCode(FhirValueSetBase):
    """
    Custom codeset for providerSearch.searchCharacteristic extension
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "SearchCharacteristicCode"]) -> None:
            self.f: Callable[..., "SearchCharacteristicCode"] = f

        def __get__(
            self, obj: Any, owner: Type["SearchCharacteristicCode"]
        ) -> "SearchCharacteristicCode":
            return self.f(owner)

    @classproperty
    def IncludeInSearch(cls) -> "SearchCharacteristicCode":
        """
        Resource populateS in front-end search results
        """
        # noinspection PyCallingNonCallable
        return SearchCharacteristicCode("searchable")

    @classproperty
    def Bookable(cls) -> "SearchCharacteristicCode":
        """
        Resource is available for appointment creations
        """
        # noinspection PyCallingNonCallable
        return SearchCharacteristicCode("bookable")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/ValueSet/search_characteristic"
