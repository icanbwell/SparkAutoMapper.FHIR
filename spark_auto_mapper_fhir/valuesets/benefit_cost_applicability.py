from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class BenefitCostApplicabilityCode(FhirValueSetBase):
    """
    Whether the cost applies to in-network or out-of-network providers.
    https://www.hl7.org/fhir/valueset-insuranceplan-applicability.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "BenefitCostApplicabilityCode"]) -> None:
            self.f: Callable[..., "BenefitCostApplicabilityCode"] = f

        def __get__(
            self, obj: Any, owner: Type["BenefitCostApplicabilityCode"]
        ) -> "BenefitCostApplicabilityCode":
            return self.f(owner)

    @classproperty
    def InNetwork(cls) -> "BenefitCostApplicabilityCode":
        """
        Provider is contracted with the health insurance company to provide
        services to plan members for specific pre-negotiated rates
        """
        # noinspection PyCallingNonCallable
        return BenefitCostApplicabilityCode("in-network")

    @classproperty
    def OutOfNetwork(cls) -> "BenefitCostApplicabilityCode":
        """
        Provider is not contracted with the health insurance company to provide services to plan
        members for specific pre-negotiated rates
        """
        # noinspection PyCallingNonCallable
        return BenefitCostApplicabilityCode("out-of-network")

    @classproperty
    def Other(cls) -> "BenefitCostApplicabilityCode":
        """
        Other applicability
        """
        # noinspection PyCallingNonCallable
        return BenefitCostApplicabilityCode("other")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/applicability
        """
        return "http://terminology.hl7.org/CodeSystem/applicability"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.0
        """
        return "2.16.840.1.113883.4.642.3.0"
