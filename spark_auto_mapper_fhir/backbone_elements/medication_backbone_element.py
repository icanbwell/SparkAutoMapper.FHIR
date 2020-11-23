from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase


class MedicationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        MedicationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#MedicationBackboneElement
        """
        super().__init__(
            id_=id_,
            extension=extension,
        )
