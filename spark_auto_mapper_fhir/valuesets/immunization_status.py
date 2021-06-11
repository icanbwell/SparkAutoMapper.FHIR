from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ImmunizationStatusCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-immunization-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ImmunizationStatusCode"]) -> None:
            self.f: Callable[..., "ImmunizationStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ImmunizationStatusCode"]
        ) -> "ImmunizationStatusCode":
            return self.f(owner)

    @classproperty
    def completed(cls) -> "ImmunizationStatusCode":
        """
        The event has now concluded
        """
        # noinspection PyCallingNonCallable
        return ImmunizationStatusCode("completed")

    @classproperty
    def EnteredInError(cls) -> "ImmunizationStatusCode":
        """
        This electronic record should never have existed, though it is
        possible that real-world decisions were based on it
        """
        # noinspection PyCallingNonCallable
        return ImmunizationStatusCode("entered-in-error")

    @classproperty
    def NotDone(cls) -> "ImmunizationStatusCode":
        """
        The event was terminated prior to any activity beyond preparation.
        I.e. The 'main' activity has not yet begun. The boundary between
        preparatory and the 'main' activity is context-specific
        """
        # noinspection PyCallingNonCallable
        return ImmunizationStatusCode("not-done")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/immunization-status
        """
        return "http://hl7.org/fhir/ValueSet/immunization-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.295
        """
        return "2.16.840.1.113883.4.642.3.295"
