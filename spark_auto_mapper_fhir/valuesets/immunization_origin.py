from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ImmunizationOriginCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-immunization-origin.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ImmunizationOriginCode"]) -> None:
            self.f: Callable[..., "ImmunizationOriginCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ImmunizationOriginCode"]
        ) -> "ImmunizationOriginCode":
            return self.f(owner)

    @classproperty
    def OtherProvider(cls) -> "ImmunizationOriginCode":
        """
        The data for the immunization event originated with another provider
        """
        # noinspection PyCallingNonCallable
        return ImmunizationOriginCode("provider")

    @classproperty
    def WrittenRecord(cls) -> "ImmunizationOriginCode":
        """
        The data for the immunization event originated with a written record for the patient
        """
        # noinspection PyCallingNonCallable
        return ImmunizationOriginCode("record")

    @classproperty
    def Recall(cls) -> "ImmunizationOriginCode":
        """
        The data for the immunization event originated from the recollection of the patient or parent/guardian of the patient
        """
        # noinspection PyCallingNonCallable
        return ImmunizationOriginCode("recall")

    @classproperty
    def SchoolRecord(cls) -> "ImmunizationOriginCode":
        """
        The data for the immunization event originated with a school record for the patient
        """
        # noinspection PyCallingNonCallable
        return ImmunizationOriginCode("school")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/immunization-origin
        """
        return "http://hl7.org/fhir/ValueSet/immunization-origin"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.296
        """
        return "2.16.840.1.113883.4.642.3.296"
