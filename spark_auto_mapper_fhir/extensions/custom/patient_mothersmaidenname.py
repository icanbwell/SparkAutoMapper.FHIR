from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class PatientMothersMaidenName(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self, url: Optional[FhirUri] = None, valueString: Optional[FhirString] = None
    ) -> None:
        """
        Extension type in FHIR
        """
        super().__init__(
            url=url or PatientMothersMaidenName.codeset, valueString=valueString
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
