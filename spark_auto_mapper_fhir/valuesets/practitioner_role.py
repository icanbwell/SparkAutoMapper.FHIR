from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class PractitionerRoleCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-practitioner-role.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "PractitionerRoleCode"]) -> None:
            self.f: Callable[..., "PractitionerRoleCode"] = f

        def __get__(
            self, obj: Any, owner: Type["PractitionerRoleCode"]
        ) -> "PractitionerRoleCode":
            return self.f(owner)

    @classproperty
    def Doctor(cls) -> "PractitionerRoleCode":
        """
        A qualified/registered medical practitioner
        """
        # noinspection PyCallingNonCallable
        return PractitionerRoleCode("doctor")

    @classproperty
    def Nurse(cls) -> "PractitionerRoleCode":
        """
        A practitioner with nursing experience that may be qualified/registered
        """
        # noinspection PyCallingNonCallable
        return PractitionerRoleCode("nurse")

    @classproperty
    def Pharmacist(cls) -> "PractitionerRoleCode":
        """
        A qualified/registered/licensed pharmacist
        """
        # noinspection PyCallingNonCallable
        return PractitionerRoleCode("pharmacist")

    @classproperty
    def Researcher(cls) -> "PractitionerRoleCode":
        """
        A practitioner that may perform research
        """
        # noinspection PyCallingNonCallable
        return PractitionerRoleCode("researcher")

    @classproperty
    def Teacher(cls) -> "PractitionerRoleCode":
        """
        Someone who is able to provide educational services
        """
        # noinspection PyCallingNonCallable
        return PractitionerRoleCode("teacher")

    @classproperty
    def ICTProfessional(cls) -> "PractitionerRoleCode":
        """
        Someone who is qualified in Information and Communication Technologies
        """
        # noinspection PyCallingNonCallable
        return PractitionerRoleCode("ict")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/practitioner-role"

    @genericclassproperty
    def codeset2(cls) -> FhirUri:
        return "http://snomed.info/sct"  # where concept is-a 223366009 (Healthcare professional)

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.439"
