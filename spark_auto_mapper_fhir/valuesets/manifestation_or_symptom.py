from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ManifestationAndSymptomCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-manifestation-or-symptom.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ManifestationAndSymptomCode"]) -> None:
            self.f: Callable[..., "ManifestationAndSymptomCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ManifestationAndSymptomCode"]
        ) -> "ManifestationAndSymptomCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ManifestationAndSymptomCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ManifestationAndSymptomCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.169
        """
        return "2.16.840.1.113883.4.642.3.169"
