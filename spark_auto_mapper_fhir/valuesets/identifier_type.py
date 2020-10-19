from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class IdentifierTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-identifier-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'IdentifierTypeCode']) -> None:
            self.f: Callable[..., 'IdentifierTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['IdentifierTypeCode']
        ) -> 'IdentifierTypeCode':
            return self.f(owner)

    @classproperty
    def SocialSecurityNumber(cls) -> 'IdentifierTypeCode':
        """
        Social Security number
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SS")

    @classproperty
    def MedicalRecordNumber(cls) -> 'IdentifierTypeCode':
        """
        An identifier that is unique to a patient within a set of medical records, not necessarily unique within an application.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MR")

    @classproperty
    def EmployeeId(cls) -> 'IdentifierTypeCode':
        """
        A number that uniquely identifies an employee to an employer.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("EI")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v2-0203"
