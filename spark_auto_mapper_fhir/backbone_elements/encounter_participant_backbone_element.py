from typing import Optional, Union

from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.valuesets.encounter_participant_type import (
    EncounterParticipantTypeCode,
)


class EncounterParticipantBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        type_: Optional[FhirList[EncounterParticipantTypeCode]] = None,
        period: Optional[Period] = None,
        individual: Optional[
            Reference[Union[Practitioner, PractitionerRole, RelatedPerson]]
        ] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        EncounterParticipantBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/encounter-definitions.html#Encounter.participant
        """
        super().__init__(
            id_=id_,
            type_=type_,
            period=period,
            individual=individual,
            extension=extension,
        )
