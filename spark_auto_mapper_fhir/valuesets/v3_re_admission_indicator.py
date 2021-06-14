from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class V3ReAdmissionIndicatorCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/v2/0092/index.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "V3ReAdmissionIndicatorCode"]) -> None:
            self.f: Callable[..., "V3ReAdmissionIndicatorCode"] = f

        def __get__(
            self, obj: Any, owner: Type["V3ReAdmissionIndicatorCode"]
        ) -> "V3ReAdmissionIndicatorCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "V3ReAdmissionIndicatorCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return V3ReAdmissionIndicatorCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/ValueSet/v2-0092
        """
        return "http://terminology.hl7.org/ValueSet/v2-0092"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """ """
        return ""
