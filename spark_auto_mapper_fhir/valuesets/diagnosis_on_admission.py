from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DiagnosisOnAdmissionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-diagnosis-on-admission.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'DiagnosisOnAdmissionCode']
        ) -> None:
            self.f: Callable[..., 'DiagnosisOnAdmissionCode'] = f

        def __get__(
            self, obj: Any, owner: Type['DiagnosisOnAdmissionCode']
        ) -> 'DiagnosisOnAdmissionCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'DiagnosisOnAdmissionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DiagnosisOnAdmissionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-diagnosis-on-admission"
