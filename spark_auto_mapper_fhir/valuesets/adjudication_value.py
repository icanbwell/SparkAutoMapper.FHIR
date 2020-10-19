from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class AdjudicationValueCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-adjudication.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'AdjudicationValueCode']) -> None:
            self.f: Callable[..., 'AdjudicationValueCode'] = f

        def __get__(
            self, obj: Any, owner: Type['AdjudicationValueCode']
        ) -> 'AdjudicationValueCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'AdjudicationValueCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return AdjudicationValueCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/adjudication"
