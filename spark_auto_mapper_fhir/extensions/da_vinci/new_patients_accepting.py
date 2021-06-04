from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.da_vinci.accepting_patients import (
    AcceptingPatientsCode,
)


class AcceptingPatientsExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, valueCodeableConcept: CodeableConcept[AcceptingPatientsCode]):
        """
        Accepting Patients
        http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients

        :param url:
        :param valueCodeableConcept:
        """
        super().__init__(
            url=AcceptingPatientsExtension.codeset,
            valueCodeableConcept=valueCodeableConcept,
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        acceptingPatients
        :return:
        :rtype:
        """
        return "acceptingPatients"
