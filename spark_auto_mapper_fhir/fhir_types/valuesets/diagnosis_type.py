from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirDiagnosisType(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-diagnosistype.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirDiagnosisType':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirDiagnosisType']) -> None:
            self.f: Callable[..., 'FhirDiagnosisType'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirDiagnosisType']
        ) -> 'FhirDiagnosisType':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirDiagnosisType':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirDiagnosisType("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-diagnosistype"
