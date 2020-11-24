from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FundsReserveCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-fundsreserve.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FundsReserveCode']) -> None:
            self.f: Callable[..., 'FundsReserveCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FundsReserveCode']
        ) -> 'FundsReserveCode':
            return self.f(owner)

    @classproperty
    def Patient(cls) -> 'FundsReserveCode':
        """
        The payor is requested to reserve funds for the provision of the named services by any provider
        for settlement of future claims related to this request.
        """
        # noinspection PyCallingNonCallable
        return FundsReserveCode("patient")

    @classproperty
    def Provider(cls) -> 'FundsReserveCode':
        """
        The payor is requested to reserve funds solely for the named provider for settlement of future claims
         related to this request.
        """
        # noinspection PyCallingNonCallable
        return FundsReserveCode("provider")

    @classproperty
    def None_(cls) -> 'FundsReserveCode':
        """
        The payor is not being requested to reserve any funds for the settlement of future claims.
        """
        # noinspection PyCallingNonCallable
        return FundsReserveCode("none")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/fundsreserve
        """
        return "http://terminology.hl7.org/CodeSystem/fundsreserve"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.33
        """
        return "2.16.840.1.113883.4.642.3.33"
