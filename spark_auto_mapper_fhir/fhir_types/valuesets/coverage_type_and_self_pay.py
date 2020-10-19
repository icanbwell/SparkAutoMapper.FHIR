from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirCoverageTypeAndSelfPayCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-coverage-type.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirCoverageTypeAndSelfPayCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirCoverageTypeAndSelfPayCode']
        ) -> None:
            self.f: Callable[..., 'FhirCoverageTypeAndSelfPayCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirCoverageTypeAndSelfPayCode']
        ) -> 'FhirCoverageTypeAndSelfPayCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirCoverageTypeAndSelfPayCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirCoverageTypeAndSelfPayCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/ValueSet/v3-ActCoverageTypeCode"

    @genericclassproperty
    def codeset_self_pay(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/coverage-selfpay"
