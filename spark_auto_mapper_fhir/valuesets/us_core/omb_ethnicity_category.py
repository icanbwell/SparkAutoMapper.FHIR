from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class OMBEthnicityCategory(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/us/core/ValueSet-omb-ethnicity-category.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "OMBEthnicityCategory"]) -> None:
            self.f: Callable[..., "OMBEthnicityCategory"] = f

        def __get__(
            self, obj: Any, owner: Type["OMBEthnicityCategory"]
        ) -> "OMBEthnicityCategory":
            return self.f(owner)

    @classproperty
    def HispanicOrLatino(cls) -> "OMBEthnicityCategory":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return OMBEthnicityCategory("2135-2")

    @classproperty
    def NonHispanicOrLatino(cls) -> "OMBEthnicityCategory":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return OMBEthnicityCategory("2186-5")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "urn:oid:2.16.840.1.113883.6.238"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.6.238"
