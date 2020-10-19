from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirRelatedPersonRelationshipTypeCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-relatedperson-relationshiptype.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirRelatedPersonRelationshipTypeCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirRelatedPersonRelationshipTypeCode']
        ) -> None:
            self.f: Callable[..., 'FhirRelatedPersonRelationshipTypeCode'] = f

        def __get__(
            self, obj: Any,
            owner: Type['FhirRelatedPersonRelationshipTypeCode']
        ) -> 'FhirRelatedPersonRelationshipTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirRelatedPersonRelationshipTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirRelatedPersonRelationshipTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v2-0131"

    @genericclassproperty
    def codeset_roles(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-RoleCode"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.449"
