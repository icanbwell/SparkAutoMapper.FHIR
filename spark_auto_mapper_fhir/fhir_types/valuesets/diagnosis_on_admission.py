from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirDiagnosisOnAdmissionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-diagnosis-on-admission.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirDiagnosisOnAdmissionCode']
        ) -> None:
            self.f: Callable[..., 'FhirDiagnosisOnAdmissionCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirDiagnosisOnAdmissionCode']
        ) -> 'FhirDiagnosisOnAdmissionCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirDiagnosisOnAdmissionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirDiagnosisOnAdmissionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-diagnosis-on-admission"
