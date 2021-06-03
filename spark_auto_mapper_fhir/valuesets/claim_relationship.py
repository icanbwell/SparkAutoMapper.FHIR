from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimRelationshipCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-related-claim-relationship.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ClaimRelationshipCode"]) -> None:
            self.f: Callable[..., "ClaimRelationshipCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ClaimRelationshipCode"]
        ) -> "ClaimRelationshipCode":
            return self.f(owner)

    @classproperty
    def PriorClaim(cls) -> "ClaimRelationshipCode":
        """
        A prior claim instance for the same intended suite of services.
        """
        # noinspection PyCallingNonCallable
        return ClaimRelationshipCode("prior")

    @classproperty
    def AssociatedClaim(cls) -> "ClaimRelationshipCode":
        """
        A claim for a different suite of services which is related the suite claimed here.
        """
        # noinspection PyCallingNonCallable
        return ClaimRelationshipCode("associated")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/ex-relatedclaimrelationship
        """
        return "http://terminology.hl7.org/CodeSystem/ex-relatedclaimrelationship"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.568
        """
        return "2.16.840.1.113883.4.642.3.568"
