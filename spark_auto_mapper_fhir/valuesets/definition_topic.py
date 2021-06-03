from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DefinitionTopicCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-definition-topic.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "DefinitionTopicCode"]) -> None:
            self.f: Callable[..., "DefinitionTopicCode"] = f

        def __get__(
            self, obj: Any, owner: Type["DefinitionTopicCode"]
        ) -> "DefinitionTopicCode":
            return self.f(owner)

    @classproperty
    def Treatment(cls) -> "DefinitionTopicCode":
        """
        The definition is related to treatment of the patient.
        """
        # noinspection PyCallingNonCallable
        return DefinitionTopicCode("treatment")

    @classproperty
    def Education(cls) -> "DefinitionTopicCode":
        """
        The definition is related to education of the patient.
        """
        # noinspection PyCallingNonCallable
        return DefinitionTopicCode("education")

    @classproperty
    def Assessment(cls) -> "DefinitionTopicCode":
        """
        The definition is related to assessment of the patient.
        """
        # noinspection PyCallingNonCallable
        return DefinitionTopicCode("assessment")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/definition-topic
        """
        return "http://hl7.org/fhir/ValueSet/definition-topic"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.794
        """
        return "2.16.840.1.113883.4.642.3.794"
