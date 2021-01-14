from typing import Optional

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.resources.media import Media


class DiagnosticReportMediaBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        link: Reference[Media],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        comment: Optional[FhirString] = None,
    ) -> None:
        """
        DiagnosticReportMediaBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/diagnosticreport-definitions.html#DiagnosticReport.media
        """
        super().__init__(
            id_=id_, extension=extension, comment=comment, link=link
        )
