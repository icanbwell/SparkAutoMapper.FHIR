from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ImmunizationSubpotentReasonCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-immunization-subpotent-reason.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ImmunizationSubpotentReasonCode"]) -> None:
            self.f: Callable[..., "ImmunizationSubpotentReasonCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ImmunizationSubpotentReasonCode"]
        ) -> "ImmunizationSubpotentReasonCode":
            return self.f(owner)

    @classproperty
    def PartialDose(cls) -> "ImmunizationSubpotentReasonCode":
        """
        The full volume of the dose was not administered to the patient.
        """
        # noinspection PyCallingNonCallable
        return ImmunizationSubpotentReasonCode("partial")

    @classproperty
    def ColdChainBreak(cls) -> "ImmunizationSubpotentReasonCode":
        """
        The vaccine experienced a cold chain break.
        """
        # noinspection PyCallingNonCallable
        return ImmunizationSubpotentReasonCode("coldchainbreak")

    @classproperty
    def ManufacturerRecall(cls) -> "ImmunizationSubpotentReasonCode":
        """
        The vaccine was recalled by the manufacturer.
        """
        # noinspection PyCallingNonCallable
        return ImmunizationSubpotentReasonCode("recall")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/immunization-subpotent-reason
        """
        return "http://hl7.org/fhir/ValueSet/immunization-subpotent-reason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.993
        """
        return "2.16.840.1.113883.4.642.3.993"
