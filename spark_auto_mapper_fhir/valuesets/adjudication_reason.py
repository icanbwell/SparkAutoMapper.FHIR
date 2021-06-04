from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class AdjudicationReasonCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-adjudication-reason.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "AdjudicationReasonCode"]) -> None:
            self.f: Callable[..., "AdjudicationReasonCode"] = f

        def __get__(
            self, obj: Any, owner: Type["AdjudicationReasonCode"]
        ) -> "AdjudicationReasonCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "AdjudicationReasonCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return AdjudicationReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/adjudication-reason"
