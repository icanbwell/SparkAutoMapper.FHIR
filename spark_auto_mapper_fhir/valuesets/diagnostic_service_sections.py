from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DiagnosticServiceSectionCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-diagnostic-service-sections.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'DiagnosticServiceSectionCode']
        ) -> None:
            self.f: Callable[..., 'DiagnosticServiceSectionCode'] = f

        def __get__(
            self, obj: Any, owner: Type['DiagnosticServiceSectionCode']
        ) -> 'DiagnosticServiceSectionCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'DiagnosticServiceSectionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DiagnosticServiceSectionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/v2-0074
        """
        return "http://terminology.hl7.org/CodeSystem/v2-0074"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.234
        """
        return "2.16.840.1.113883.4.642.3.234"
