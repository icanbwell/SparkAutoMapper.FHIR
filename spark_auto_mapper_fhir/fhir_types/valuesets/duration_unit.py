from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirDurationUnitCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-duration-units.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirDurationUnitCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirDurationUnitCode']) -> None:
            self.f: Callable[..., 'FhirDurationUnitCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirDurationUnitCode']
        ) -> 'FhirDurationUnitCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirDurationUnitCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirDurationUnitCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://unitsofmeasure.org"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.61"
