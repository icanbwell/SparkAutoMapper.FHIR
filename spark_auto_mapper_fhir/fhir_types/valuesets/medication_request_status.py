from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirMedicationRequestStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-medicationrequest-status.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirMedicationRequestStatusCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirMedicationRequestStatusCode']
        ) -> None:
            self.f: Callable[..., 'FhirMedicationRequestStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirMedicationRequestStatusCode']
        ) -> 'FhirMedicationRequestStatusCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirMedicationRequestStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirMedicationRequestStatusCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/CodeSystem/medicationrequest-status"
