from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DiagnosisRelatedGroupCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-diagnosisrelatedgroup.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'DiagnosisRelatedGroupCode']
        ) -> None:
            self.f: Callable[..., 'DiagnosisRelatedGroupCode'] = f

        def __get__(
            self, obj: Any, owner: Type['DiagnosisRelatedGroupCode']
        ) -> 'DiagnosisRelatedGroupCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'DiagnosisRelatedGroupCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRelatedGroupCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup"
