from __future__ import annotations
from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

class $ClassName(FhirBackboneElementBase):
    def __init__(self,*,id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None) -> None:
        """
        $ClassName Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR 
                    properties not just the ones you need
        $Documentation
        """
        super().__init__(
            id_=id_,
            extension=extension
         )
