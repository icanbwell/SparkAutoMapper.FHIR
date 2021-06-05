from typing import Optional

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase

from spark_auto_mapper_fhir.backbone_elements.stratum_backbone_element import (
    StratumBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)


class StratifierBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        code: Optional[FhirList[CodeableConcept[FhirValueSetBase]]] = None,
        stratum: Optional[FhirList[StratumBackboneElement]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        StratifierBackboneElement Resource in FHIR
        https://www.hl7.org/fhir/measurereport.html#MeasureReport.stratifier


        :param code: What stratifier of the group
        :param stratum: Stratum results, one for each unique value, or set of values, in the stratifier, or stratifier components
        """
        super().__init__(
            id_=id_,
            code=code,
            stratum=stratum,
            extension=extension,
        )
