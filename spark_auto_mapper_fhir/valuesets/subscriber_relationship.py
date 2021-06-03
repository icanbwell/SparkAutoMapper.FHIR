from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SubscriberRelationshipCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-subscriber-relationship.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "SubscriberRelationshipCode"]) -> None:
            self.f: Callable[..., "SubscriberRelationshipCode"] = f

        def __get__(
            self, obj: Any, owner: Type["SubscriberRelationshipCode"]
        ) -> "SubscriberRelationshipCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "SubscriberRelationshipCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SubscriberRelationshipCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/subscriber-relationship"
