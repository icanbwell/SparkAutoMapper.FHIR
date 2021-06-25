from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DetailedEthnicity(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/us/core/ValueSet-detailed-ethnicity.html
    All codes from https://www.hl7.org/fhir/us/core/CodeSystem-cdcrec.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "DetailedEthnicity"]) -> None:
            self.f: Callable[..., "DetailedEthnicity"] = f

        def __get__(
            self, obj: Any, owner: Type["DetailedEthnicity"]
        ) -> "DetailedEthnicity":
            return self.f(owner)

    @classproperty
    def Mexican(cls) -> "DetailedEthnicity":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DetailedEthnicity("2148-5")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "urn:oid:2.16.840.1.113883.6.238"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.6.238"
