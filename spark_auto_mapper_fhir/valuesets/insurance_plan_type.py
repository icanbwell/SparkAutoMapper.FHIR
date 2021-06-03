from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class InsurancePlanTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-insuranceplan-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "InsurancePlanTypeCode"]) -> None:
            self.f: Callable[..., "InsurancePlanTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["InsurancePlanTypeCode"]
        ) -> "InsurancePlanTypeCode":
            return self.f(owner)

    @classproperty
    def Medical(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("medical")

    @classproperty
    def Dental(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("dental")

    @classproperty
    def MentalHealth(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("mental")

    @classproperty
    def SubstanceAbuse(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("subst-ab")

    @classproperty
    def Vision(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("vision")

    @classproperty
    def Drug(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("drug")

    @classproperty
    def ShortTermCare(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("short-term")

    @classproperty
    def LongTermCare(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("long-term")

    @classproperty
    def Hospice(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("hospice")

    @classproperty
    def HomeHealth(cls) -> "InsurancePlanTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return InsurancePlanTypeCode("home")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/insurance-plan-type
        """
        return "http://terminology.hl7.org/CodeSystem/insurance-plan-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.870
        """
        return "2.16.840.1.113883.4.642.3.870"
