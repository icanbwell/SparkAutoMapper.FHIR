from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirAccidentIncidentCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v3/ActIncidentCode/vs.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirAccidentIncidentCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirAccidentIncidentCode']
        ) -> None:
            self.f: Callable[..., 'FhirAccidentIncidentCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirAccidentIncidentCode']
        ) -> 'FhirAccidentIncidentCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirAccidentIncidentCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirAccidentIncidentCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-ActCode"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.1.11.16508"
