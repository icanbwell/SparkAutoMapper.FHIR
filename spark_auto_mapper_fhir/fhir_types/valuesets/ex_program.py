from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirExProgramReasonCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-program-code.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirExProgramReasonCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirExProgramReasonCode']
        ) -> None:
            self.f: Callable[..., 'FhirExProgramReasonCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirExProgramReasonCode']
        ) -> 'FhirExProgramReasonCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirExProgramReasonCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirExProgramReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-programcode"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.576"
