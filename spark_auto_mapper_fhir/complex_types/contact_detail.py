from typing import Optional

from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)


class ContactDetail(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        name: Optional[FhirString] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
    ) -> None:
        """
        ContactDetail Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes-definitions.html#ContactDetail
        """
        super().__init__(id_=id_, extension=extension, name=name, telecom=telecom)
