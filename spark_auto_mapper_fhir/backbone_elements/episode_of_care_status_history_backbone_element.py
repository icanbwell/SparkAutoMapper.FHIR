from typing import Optional

from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.valuesets.episode_of_care_status import (
    EpisodeOfCareStatusCode,
)


class EpisodeOfCareStatusHistoryBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        status: EpisodeOfCareStatusCode,
        period: Period,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        EpisodeOfCareStatusHistoryBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/episodeofcare-definitions.html#EpisodeOfCare.statusHistory
        """
        super().__init__(id_=id_, status=status, period=period, extension=extension)
