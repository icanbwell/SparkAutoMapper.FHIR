from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class Icd10Code(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-icd-10.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "Icd10Code"]) -> None:
            self.f: Callable[..., "Icd10Code"] = f

        def __get__(self, obj: Any, owner: Type["Icd10Code"]) -> "Icd10Code":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "Icd10Code":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return Icd10Code("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/sid/icd-10"
