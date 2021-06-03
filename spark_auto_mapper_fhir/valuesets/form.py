from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FormCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-forms.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "FormCode"]) -> None:
            self.f: Callable[..., "FormCode"] = f

        def __get__(self, obj: Any, owner: Type["FormCode"]) -> "FormCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "FormCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FormCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/forms-codes"
