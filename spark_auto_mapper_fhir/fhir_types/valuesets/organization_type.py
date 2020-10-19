from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirOrganizationTypeCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-organization-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirOrganizationTypeCode']
        ) -> None:
            self.f: Callable[..., 'FhirOrganizationTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirOrganizationTypeCode']
        ) -> 'FhirOrganizationTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirOrganizationTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirOrganizationTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/organization-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.414"
