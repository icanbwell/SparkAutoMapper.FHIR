from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SortDirectionCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-sort-direction.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "SortDirectionCode"]) -> None:
            self.f: Callable[..., "SortDirectionCode"] = f

        def __get__(
            self, obj: Any, owner: Type["SortDirectionCode"]
        ) -> "SortDirectionCode":
            return self.f(owner)

    @classproperty
    def Ascending(cls) -> "SortDirectionCode":
        """
        Sort by the value ascending, so that lower values appear first.
        """
        # noinspection PyCallingNonCallable
        return SortDirectionCode("ascending")

    @classproperty
    def Descending(cls) -> "SortDirectionCode":
        """
        Sort by the value descending, so that lower values appear last.
        """
        # noinspection PyCallingNonCallable
        return SortDirectionCode("descending")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/sort-direction
        """
        return "http://hl7.org/fhir/ValueSet/sort-direction"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.979
        """
        return "2.16.840.1.113883.4.642.3.979"
