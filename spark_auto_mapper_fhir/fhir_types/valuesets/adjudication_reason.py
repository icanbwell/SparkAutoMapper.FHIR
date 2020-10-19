from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirAdjudicationReasonCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-adjudication-reason.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirAdjudicationReasonCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirAdjudicationReasonCode']
        ) -> None:
            self.f: Callable[..., 'FhirAdjudicationReasonCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirAdjudicationReasonCode']
        ) -> 'FhirAdjudicationReasonCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirAdjudicationReasonCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirAdjudicationReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/adjudication-reason"
