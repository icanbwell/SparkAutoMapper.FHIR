from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ObservationReferenceRangeMeaningCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-referencerange-meaning.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., "ObservationReferenceRangeMeaningCode"]
        ) -> None:
            self.f: Callable[..., "ObservationReferenceRangeMeaningCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ObservationReferenceRangeMeaningCode"]
        ) -> "ObservationReferenceRangeMeaningCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ObservationReferenceRangeMeaningCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ObservationReferenceRangeMeaningCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/referencerange-meaning
        """
        return "http://terminology.hl7.org/CodeSystem/referencerange-meaning"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.397
        """
        return "2.16.840.1.113883.4.642.3.397"
