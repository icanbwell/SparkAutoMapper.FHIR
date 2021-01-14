from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class RelatedArtifactTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-related-artifact-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'RelatedArtifactTypeCode']
        ) -> None:
            self.f: Callable[..., 'RelatedArtifactTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['RelatedArtifactTypeCode']
        ) -> 'RelatedArtifactTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'RelatedArtifactTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return RelatedArtifactTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/related-artifact-type
        """
        return "http://hl7.org/fhir/ValueSet/related-artifact-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.99
        """
        return "2.16.840.1.113883.4.642.3.99"
