from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class RelatedPersonRelationshipTypeCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-relatedperson-relationshiptype.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'RelatedPersonRelationshipTypeCode']
        ) -> None:
            self.f: Callable[..., 'RelatedPersonRelationshipTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['RelatedPersonRelationshipTypeCode']
        ) -> 'RelatedPersonRelationshipTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'RelatedPersonRelationshipTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return RelatedPersonRelationshipTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v2-0131"

    @genericclassproperty
    def codeset_roles(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-RoleCode"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.449"
