from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ImmunizationTargetDiseaseCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-immunization-target-disease.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ImmunizationTargetDiseaseCode"]) -> None:
            self.f: Callable[..., "ImmunizationTargetDiseaseCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ImmunizationTargetDiseaseCode"]
        ) -> "ImmunizationTargetDiseaseCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ImmunizationTargetDiseaseCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ImmunizationTargetDiseaseCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/immunization-target-disease
        """
        return "http://hl7.org/fhir/ValueSet/immunization-target-disease"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.1047
        """
        return "2.16.840.1.113883.4.642.3.1047"
