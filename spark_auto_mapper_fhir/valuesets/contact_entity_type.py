from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ContactEntityTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-contactentity-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ContactEntityTypeCode']) -> None:
            self.f: Callable[..., 'ContactEntityTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ContactEntityTypeCode']
        ) -> 'ContactEntityTypeCode':
            return self.f(owner)

    @classproperty
    def Billing(cls) -> 'ContactEntityTypeCode':
        """
        Contact details for information regarding to billing/general finance enquiries.
        """
        # noinspection PyCallingNonCallable
        return ContactEntityTypeCode("BILL")

    @classproperty
    def Administrative(cls) -> 'ContactEntityTypeCode':
        """
        Contact details for administrative enquiries.
        """
        # noinspection PyCallingNonCallable
        return ContactEntityTypeCode("ADMIN")

    @classproperty
    def HumanResource(cls) -> 'ContactEntityTypeCode':
        """
        Contact details for issues related to Human Resources, such as staff matters, OH&S etc.
        """
        # noinspection PyCallingNonCallable
        return ContactEntityTypeCode("HR")

    # noinspection SpellCheckingInspection
    @classproperty
    def Payor(cls) -> 'ContactEntityTypeCode':
        """
        Contact details for dealing with issues related to insurance claims/adjudication/payment.
        """
        # noinspection PyCallingNonCallable
        return ContactEntityTypeCode("PAYOR")

    @classproperty
    def Patient(cls) -> 'ContactEntityTypeCode':
        """
        Generic information contact for patients.
        """
        # noinspection PyCallingNonCallable,SpellCheckingInspection
        return ContactEntityTypeCode("PATINF")

    @classproperty
    def Press(cls) -> 'ContactEntityTypeCode':
        """
        Dedicated contact point for matters relating to press enquiries.
        """
        # noinspection PyCallingNonCallable
        return ContactEntityTypeCode("PRESS")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/contactentity-type
        """
        return "http://terminology.hl7.org/CodeSystem/contactentity-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.416
        """
        return "2.16.840.1.113883.4.642.3.416"
