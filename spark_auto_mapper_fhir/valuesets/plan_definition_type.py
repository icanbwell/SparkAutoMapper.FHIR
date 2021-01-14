from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class PlanDefinitionTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-plan-definition-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'PlanDefinitionTypeCode']) -> None:
            self.f: Callable[..., 'PlanDefinitionTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['PlanDefinitionTypeCode']
        ) -> 'PlanDefinitionTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'PlanDefinitionTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return PlanDefinitionTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/plan-definition-type
        """
        return "http://hl7.org/fhir/ValueSet/plan-definition-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.797
        """
        return "2.16.840.1.113883.4.642.3.797"
