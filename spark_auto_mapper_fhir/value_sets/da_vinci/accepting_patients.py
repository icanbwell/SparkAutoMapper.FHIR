from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class AcceptingPatientsCode(GenericTypeCode):
    """
    https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/CodeSystem-AcceptingPatientsCS.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    codeset: FhirUri = "https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/CodeSystem-AcceptingPatientsCS.html"


class AcceptingPatientsCodeValues:
    """
    Not accepting patients
    """

    NotAccepting = AcceptingPatientsCode("nopt")

    """
    Accepting new patients
    """
    Accepting = AcceptingPatientsCode("newpt")

    """
    Accepting existing patients
    """
    AcceptingExistingPatients = AcceptingPatientsCode("existptonly")

    """
    Accepting existing patients and members of their families
    """
    AcceptingExistingPatientsAndTheirFamilies = AcceptingPatientsCode("existptfam")
