from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType
from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase


class AcceptingPatientsCode(FhirValueSetBase):
    """
    https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/CodeSystem-AcceptingPatientsCS.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "AcceptingPatientsCode"]) -> None:
            self.f: Callable[..., "AcceptingPatientsCode"] = f

        def __get__(
            self, obj: Any, owner: Type["AcceptingPatientsCode"]
        ) -> "AcceptingPatientsCode":
            return self.f(owner)

    @classproperty
    def NotAccepting(cls) -> "AcceptingPatientsCode":
        """
        Not accepting patients
        """
        # noinspection PyCallingNonCallable
        return AcceptingPatientsCode("nopt")

    @classproperty
    def Accepting(cls) -> "AcceptingPatientsCode":
        """
        Accepting new patients
        """
        # noinspection PyCallingNonCallable
        return AcceptingPatientsCode("newpt")

    @classproperty
    def AcceptingExistingPatients(cls) -> "AcceptingPatientsCode":
        """
        Accepting existing patients
        """
        # noinspection PyCallingNonCallable
        return AcceptingPatientsCode("existptonly")

    @classproperty
    def AcceptingExistingPatientsAndTheirFamilies(cls) -> "AcceptingPatientsCode":
        """
        Accepting existing patients and members of their families
        """
        # noinspection PyCallingNonCallable
        return AcceptingPatientsCode("existptfam")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/CodeSystem-AcceptingPatientsCS.html"
