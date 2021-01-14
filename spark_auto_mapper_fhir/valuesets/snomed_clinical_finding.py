from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SNOMEDCTClinicalFindingsCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-clinical-findings.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'SNOMEDCTClinicalFindingsCode']
        ) -> None:
            self.f: Callable[..., 'SNOMEDCTClinicalFindingsCode'] = f

        def __get__(
            self, obj: Any, owner: Type['SNOMEDCTClinicalFindingsCode']
        ) -> 'SNOMEDCTClinicalFindingsCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'SNOMEDCTClinicalFindingsCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SNOMEDCTClinicalFindingsCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/clinical-findings
        """
        return "http://hl7.org/fhir/ValueSet/clinical-findings"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.232
        """
        return "2.16.840.1.113883.4.642.3.232"
