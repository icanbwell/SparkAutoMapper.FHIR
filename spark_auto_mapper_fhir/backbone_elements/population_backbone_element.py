from typing import Optional

from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.measure_population import MeasurePopulationTypeCode


class PopulationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        code: Optional[CodeableConcept[MeasurePopulationTypeCode]] = None,
        count: Optional[FhirInteger] = None,
        # subjectResults: Optional[Reference[List]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        super().__init__(
            id_=id_,
            code=code,
            count=count,
            # subjectResults=subjectResults,
            extension=extension,
        )
