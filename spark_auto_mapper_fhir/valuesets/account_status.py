from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class AccountStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-account-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "AccountStatusCode"]) -> None:
            self.f: Callable[..., "AccountStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["AccountStatusCode"]
        ) -> "AccountStatusCode":
            return self.f(owner)

    @classproperty
    def Active(cls) -> "AccountStatusCode":
        """
        This account is active and may be used
        """
        # noinspection PyCallingNonCallable
        return AccountStatusCode("active")

    @classproperty
    def Inactive(cls) -> "AccountStatusCode":
        """
        This account is inactive and should not be used to track financial information
        """
        # noinspection PyCallingNonCallable
        return AccountStatusCode("inactive")

    @classproperty
    def EnteredInError(cls) -> "AccountStatusCode":
        """
        This instance should not have been part of this patient's medical record
        """
        # noinspection PyCallingNonCallable
        return AccountStatusCode("entered-in-error")

    @classproperty
    def OnHold(cls) -> "AccountStatusCode":
        """
        The account is on hold.
        """
        # noinspection PyCallingNonCallable
        return AccountStatusCode("on-hold")

    @classproperty
    def Unknown(cls) -> "AccountStatusCode":
        """
        The account status is unknown.
        """
        # noinspection PyCallingNonCallable
        return AccountStatusCode("unknown")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/account-status

        """
        return "http://hl7.org/fhir/ValueSet/account-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.726
        """
        return "2.16.840.1.113883.4.642.3.726"
