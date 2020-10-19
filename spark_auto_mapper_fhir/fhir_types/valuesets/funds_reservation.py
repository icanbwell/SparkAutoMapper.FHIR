from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirFundsReservationCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-fundsreserve.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirFundsReservationCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirFundsReservationCode']
        ) -> None:
            self.f: Callable[..., 'FhirFundsReservationCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirFundsReservationCode']
        ) -> 'FhirFundsReservationCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirFundsReservationCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirFundsReservationCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/fundsreserve"