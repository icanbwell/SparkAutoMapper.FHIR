from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ObservationMethodsCode(FhirValueSetBase):
    """
    Observation Method codes from SNOMED CT  where concept is-a 272394005 (Technique (qualifier value))
    or is-a 129264002 (Action (qualifier value)) or is-a 386053000 (Evaluation procedure(procedure))
    https://www.hl7.org/fhir/valueset-observation-methods.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ObservationMethodsCode"]) -> None:
            self.f: Callable[..., "ObservationMethodsCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ObservationMethodsCode"]
        ) -> "ObservationMethodsCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ObservationMethodsCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ObservationMethodsCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.395
        """
        return "2.16.840.1.113883.4.642.3.395"
