from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MedicationAsNeededReasonCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-medication-as-needed-reason.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "MedicationAsNeededReasonCode"]) -> None:
            self.f: Callable[..., "MedicationAsNeededReasonCode"] = f

        def __get__(
            self, obj: Any, owner: Type["MedicationAsNeededReasonCode"]
        ) -> "MedicationAsNeededReasonCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "MedicationAsNeededReasonCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return MedicationAsNeededReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/ValueSet/medication-as-needed-reason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.96"
