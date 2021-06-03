from typing import Optional

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class StratumComponentBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        code: CodeableConcept[FhirValueSetBase],
        value: CodeableConcept[FhirValueSetBase],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        StratumComponentBackboneElement Resource in FHIR
        https://www.hl7.org/fhir/measurereport.html#MeasureReport.stratifier.stratum.component


        :param code: What stratifier component of the group
        :param value: The stratum component value, e.g. male
        """
        super().__init__(
            code=code,
            value=value,
            id_=id_,
            extension=extension,
        )
