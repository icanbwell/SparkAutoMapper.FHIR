from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class PracticeSettingCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-c80-practice-codes.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "PracticeSettingCode"]) -> None:
            self.f: Callable[..., "PracticeSettingCode"] = f

        def __get__(
            self, obj: Any, owner: Type["PracticeSettingCode"]
        ) -> "PracticeSettingCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "PracticeSettingCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return PracticeSettingCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://nucc.org/provider-taxonomy
        """
        return "http://nucc.org/provider-taxonomy"

    @genericclassproperty
    def codeset_snomed(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.3.88.12.80.72"
