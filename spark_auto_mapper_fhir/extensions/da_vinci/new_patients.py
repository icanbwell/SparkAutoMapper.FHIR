from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.classproperty import genericclassproperty

from spark_auto_mapper_fhir.extensions.da_vinci.new_patients_accepting import (
    AcceptingPatientsExtension,
)
from spark_auto_mapper_fhir.extensions.da_vinci.new_patients_characteristics import (
    CharacteristicExtension,
)
from spark_auto_mapper_fhir.extensions.da_vinci.new_patients_from_network import (
    FromNetworkExtension,
)
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class NewPatientsExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        acceptingPatients: AcceptingPatientsExtension,
        fromNetwork: Optional[FromNetworkExtension] = None,
        characteristics: Optional[FhirList[CharacteristicExtension]] = None,
        id_: Optional[FhirId] = None,
    ) -> None:
        """
        New Patients indicates whether new patients are being accepted in general, or from a specific network.
        This extension is included in the PractitionerRole, HealthcareService, and Location profiles.
        This provides needed flexibility for specifying whether a provider accepts new patients by location and network.

        :param acceptingPatients: Accepting Patients
        :param fromNetwork: From Network
        :param characteristics: Characteristics of accepted patients
        """

        super().__init__(
            url=NewPatientsExtension.codeset,
            id_=id_,
            extension=[acceptingPatients, fromNetwork, characteristics],
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients
        :return:
        :rtype:
        """
        return "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients"
