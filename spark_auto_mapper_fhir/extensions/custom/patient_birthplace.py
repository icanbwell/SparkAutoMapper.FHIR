from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class PatientBirthPlace(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self, url: Optional[FhirUri] = None, valueAddress: Optional[Address] = None
    ) -> None:
        """
        Extension type in FHIR
        """
        super().__init__(
            url=url or PatientBirthPlace.codeset, valueAddress=valueAddress
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/StructureDefinition/patient-birthPlace"
