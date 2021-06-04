from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SubjectTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-subject-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "SubjectTypeCode"]) -> None:
            self.f: Callable[..., "SubjectTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["SubjectTypeCode"]
        ) -> "SubjectTypeCode":
            return self.f(owner)

    @classproperty
    def Patient(cls) -> "SubjectTypeCode":
        """
        Demographics and other administrative information about an individual or animal receiving care
        or other health-related services.
        """
        # noinspection PyCallingNonCallable
        return SubjectTypeCode("Patient")

    @classproperty
    def Practitioner(cls) -> "SubjectTypeCode":
        """
        A person who is directly or indirectly involved in the provisioning of healthcare.
        """
        # noinspection PyCallingNonCallable
        return SubjectTypeCode("Practitioner")

    @classproperty
    def Organization(cls) -> "SubjectTypeCode":
        """
        A formally or informally recognized grouping of people or organizations formed for the purpose of achieving
         some form of collective action. Includes companies, institutions, corporations, departments, community groups,
          healthcare practice groups, payer/insurer, etc.
        """
        # noinspection PyCallingNonCallable
        return SubjectTypeCode("Organization")

    @classproperty
    def Location(cls) -> "SubjectTypeCode":
        """
        Details and position information for a physical place where services are provided and resources and
        participants may be stored, found, contained, or accommodated.
        """
        # noinspection PyCallingNonCallable
        return SubjectTypeCode("Location")

    @classproperty
    def Device(cls) -> "SubjectTypeCode":
        """
        A type of a manufactured item that is used in the provision of healthcare without being substantially changed
         through that activity. The device may be a medical or non-medical device.
        """
        # noinspection PyCallingNonCallable
        return SubjectTypeCode("Device")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/subject-type
        """
        return "http://hl7.org/fhir/ValueSet/subject-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.775
        """
        return "2.16.840.1.113883.4.642.3.775"
