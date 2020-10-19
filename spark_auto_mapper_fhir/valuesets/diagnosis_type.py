from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DiagnosisTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-diagnosistype.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'DiagnosisTypeCode']) -> None:
            self.f: Callable[..., 'DiagnosisTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['DiagnosisTypeCode']
        ) -> 'DiagnosisTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'DiagnosisTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-diagnosistype"
