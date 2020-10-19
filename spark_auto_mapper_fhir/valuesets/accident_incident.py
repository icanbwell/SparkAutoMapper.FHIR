from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class AccidentIncidentCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v3/ActIncidentCode/vs.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'AccidentIncidentCode']) -> None:
            self.f: Callable[..., 'AccidentIncidentCode'] = f

        def __get__(
            self, obj: Any, owner: Type['AccidentIncidentCode']
        ) -> 'AccidentIncidentCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'AccidentIncidentCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return AccidentIncidentCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-ActCode"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.1.11.16508"
