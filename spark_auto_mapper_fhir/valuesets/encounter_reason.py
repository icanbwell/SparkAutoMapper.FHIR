from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterReasonCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-encounter-reason.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterReasonCode"]) -> None:
            self.f: Callable[..., "EncounterReasonCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterReasonCode"]
        ) -> "EncounterReasonCode":
            return self.f(owner)

    @classproperty
    def NameYourFirstValue(cls) -> "EncounterReasonCode":
        """ """
        # noinspection PyCallingNonCallable
        return EncounterReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-reason
        """
        return "http://hl7.org/fhir/ValueSet/encounter-reason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.261
        """
        return "2.16.840.1.113883.4.642.3.261"