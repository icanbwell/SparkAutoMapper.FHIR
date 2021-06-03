from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class V2AppointmentReasonCode(FhirValueSetBase):
    """
    http://terminology.hl7.org/ValueSet/v2-0276
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "V2AppointmentReasonCode"]) -> None:
            self.f: Callable[..., "V2AppointmentReasonCode"] = f

        def __get__(
            self, obj: Any, owner: Type["V2AppointmentReasonCode"]
        ) -> "V2AppointmentReasonCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "V2AppointmentReasonCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return V2AppointmentReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v2-0276"
