from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SnoMedCode(FhirValueSetBase):
    """
    http://snomed.info/sct
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'SnoMedCode']) -> None:
            self.f: Callable[..., 'SnoMedCode'] = f

        def __get__(self, obj: Any, owner: Type['SnoMedCode']) -> 'SnoMedCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'SnoMedCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SnoMedCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        """
        return ""
