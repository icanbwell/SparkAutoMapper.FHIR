from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class CareTeamStatusCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://www.hl7.org/fhir/valueset-care-team-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "CareTeamStatusCode"]) -> None:
            self.f: Callable[..., "CareTeamStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["CareTeamStatusCode"]
        ) -> "CareTeamStatusCode":
            return self.f(owner)

    @classproperty
    def Proposed(cls) -> "CareTeamStatusCode":
        """
        The care team has been drafted and proposed, but not yet participating in the coordination and delivery of patient care.
        """
        # noinspection PyCallingNonCallable
        return CareTeamStatusCode("proposed")

    @classproperty
    def Active(cls) -> "CareTeamStatusCode":
        """
        The care team is currently participating in the coordination and delivery of care.
        """
        # noinspection PyCallingNonCallable
        return CareTeamStatusCode("active")

    @classproperty
    def Suspended(cls) -> "CareTeamStatusCode":
        """
        The care team is temporarily on hold or suspended and not participating in the coordination and delivery of care.
        """
        # noinspection PyCallingNonCallable
        return CareTeamStatusCode("suspended")

    @classproperty
    def Inactive(cls) -> "CareTeamStatusCode":
        """
        The care team was, but is no longer, participating in the coordination and delivery of care.
        """
        # noinspection PyCallingNonCallable
        return CareTeamStatusCode("inactive")

    @classproperty
    def EnteredInError(cls) -> "CareTeamStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return CareTeamStatusCode("entered-in-error")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/care-team-status
        """
        return "http://hl7.org/fhir/care-team-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.153
        """
        return "2.16.840.1.113883.4.642.3.153"
