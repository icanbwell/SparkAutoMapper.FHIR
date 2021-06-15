from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class VaccineCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-vaccine-code.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "VaccineCode"]) -> None:
            self.f: Callable[..., "VaccineCode"] = f

        def __get__(self, obj: Any, owner: Type["VaccineCode"]) -> "VaccineCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "VaccineCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return VaccineCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/vaccine-code
        """
        return "http://hl7.org/fhir/ValueSet/vaccine-code"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.3.88.12.80.22
        """
        return "2.16.840.1.113883.3.88.12.80.22"
