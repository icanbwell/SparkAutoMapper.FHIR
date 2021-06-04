from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class AdjudicationValueCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-adjudication.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "AdjudicationValueCode"]) -> None:
            self.f: Callable[..., "AdjudicationValueCode"] = f

        def __get__(
            self, obj: Any, owner: Type["AdjudicationValueCode"]
        ) -> "AdjudicationValueCode":
            return self.f(owner)

    @classproperty
    def SubmittedAmount(cls) -> "AdjudicationValueCode":
        """
        The total submitted amount for the claim or group or line item.
        """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("submitted")

    def CoPay(cls) -> "AdjudicationValueCode":
        """
        Patient Co-Payment
        """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("copay")

    def EligibleAmount(cls) -> "AdjudicationValueCode":
        """
        Amount of the change which is considered for adjudication.
        """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("eligible")

    def Deductible(cls) -> "AdjudicationValueCode":
        """
        Amount deducted from the eligible amount prior to adjudication.
        """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("deductible")

    def BenefitAmount(cls) -> "AdjudicationValueCode":
        """
        Amount payable under the coverage.
        """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("benefit")

    def CoInsurance(cls) -> "AdjudicationValueCode":
        """ """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("coins")

    def PaidToProvider(cls) -> "AdjudicationValueCode":
        """ """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("paidtoprovider")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/adjudication"
