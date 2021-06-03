from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class AdditionalDosageInstructionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-additional-instruction-codes.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "AdditionalDosageInstructionCode"]) -> None:
            self.f: Callable[..., "AdditionalDosageInstructionCode"] = f

        def __get__(
            self, obj: Any, owner: Type["AdditionalDosageInstructionCode"]
        ) -> "AdditionalDosageInstructionCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "AdditionalDosageInstructionCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return AdditionalDosageInstructionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://snomed.info/sct "
