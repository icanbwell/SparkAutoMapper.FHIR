from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirRelatedClaimRelationshipCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-related-claim-relationship.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirRelatedClaimRelationshipCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirRelatedClaimRelationshipCode']
        ) -> None:
            self.f: Callable[..., 'FhirRelatedClaimRelationshipCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirRelatedClaimRelationshipCode']
        ) -> 'FhirRelatedClaimRelationshipCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirRelatedClaimRelationshipCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirRelatedClaimRelationshipCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.568"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-relatedclaimrelationship"
