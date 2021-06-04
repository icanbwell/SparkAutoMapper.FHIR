from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ReferralMethodCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-service-referral-method.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ReferralMethodCode"]) -> None:
            self.f: Callable[..., "ReferralMethodCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ReferralMethodCode"]
        ) -> "ReferralMethodCode":
            return self.f(owner)

    @classproperty
    def Fax(cls) -> "ReferralMethodCode":
        """
        Referrals may be accepted by fax.
        """
        # noinspection PyCallingNonCallable
        return ReferralMethodCode("fax")

    @classproperty
    def Phone(cls) -> "ReferralMethodCode":
        """
        Referrals may be accepted over the phone from a practitioner.
        """
        # noinspection PyCallingNonCallable
        return ReferralMethodCode("phone")

    @classproperty
    def SecureMessaging(cls) -> "ReferralMethodCode":
        """
        Referrals may be accepted via a secure messaging system. To determine the types of secure messaging systems
        supported, refer to the identifiers collection. Callers will need to understand the specific identifier
        system used to know that they are able to transmit messages.
        """
        # noinspection PyCallingNonCallable
        return ReferralMethodCode("elec")

    @classproperty
    def SecureEmail(cls) -> "ReferralMethodCode":
        """
        Referrals may be accepted via a secure email. To send please encrypt with the services public key.
        """
        # noinspection PyCallingNonCallable
        return ReferralMethodCode("semail")

    @classproperty
    def Mail(cls) -> "ReferralMethodCode":
        """
        Referrals may be accepted via regular postage (or hand delivered).
        """
        # noinspection PyCallingNonCallable
        return ReferralMethodCode("mail")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/service-referral-method
        """
        return "http://terminology.hl7.org/CodeSystem/service-referral-method"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.510
        """
        return "2.16.840.1.113883.4.642.3.510"
