from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ObservationReferenceRangeAppliesToCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-referencerange-appliesto.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., "ObservationReferenceRangeAppliesToCode"]
        ) -> None:
            self.f: Callable[..., "ObservationReferenceRangeAppliesToCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ObservationReferenceRangeAppliesToCode"]
        ) -> "ObservationReferenceRangeAppliesToCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ObservationReferenceRangeAppliesToCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ObservationReferenceRangeAppliesToCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/ValueSet/v3-Race
        """
        return "http://terminology.hl7.org/ValueSet/v3-Race"

    @genericclassproperty
    def codeset2(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct "

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.407
        """
        return "2.16.840.1.113883.4.642.3.407"
