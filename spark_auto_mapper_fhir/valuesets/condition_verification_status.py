from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ConditionVerificationStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-condition-ver-status.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'ConditionVerificationStatusCode']
        ) -> None:
            self.f: Callable[..., 'ConditionVerificationStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ConditionVerificationStatusCode']
        ) -> 'ConditionVerificationStatusCode':
            return self.f(owner)

    @classproperty
    def Unconfirmed(cls) -> 'ConditionVerificationStatusCode':
        """
        There is not sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
        """
        # noinspection PyCallingNonCallable
        return ConditionVerificationStatusCode("unconfirmed")

    @classproperty
    def Provisional(cls) -> 'ConditionVerificationStatusCode':
        """
        This is a tentative diagnosis - still a candidate that is under consideration.
        """
        # noinspection PyCallingNonCallable
        return ConditionVerificationStatusCode("provisional")

    @classproperty
    def Differential(cls) -> 'ConditionVerificationStatusCode':
        """
        One of a set of potential (and typically mutually exclusive) diagnoses asserted to further guide
         the diagnostic process and preliminary treatment.
        """
        # noinspection PyCallingNonCallable
        return ConditionVerificationStatusCode("differential")

    @classproperty
    def Confirmed(cls) -> 'ConditionVerificationStatusCode':
        """
        There is sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
        """
        # noinspection PyCallingNonCallable
        return ConditionVerificationStatusCode("confirmed")

    @classproperty
    def Refuted(cls) -> 'ConditionVerificationStatusCode':
        """
        This condition has been ruled out by diagnostic and clinical evidence.
        """
        # noinspection PyCallingNonCallable
        return ConditionVerificationStatusCode("refuted")

    @classproperty
    def EnteredInError(cls) -> 'ConditionVerificationStatusCode':
        """
        The statement was entered in error and is not valid.
        """
        # noinspection PyCallingNonCallable
        return ConditionVerificationStatusCode("entered-in-error")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/condition-ver-status
        """
        return "http://terminology.hl7.org/CodeSystem/condition-ver-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.166
        """
        return "2.16.840.1.113883.4.642.3.166"
