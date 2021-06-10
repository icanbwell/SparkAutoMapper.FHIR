from typing import Optional
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class ImmunizationEducationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        documentType: Optional[FhirString] = None,
        reference: Optional[FhirUri] = None,
        publicationDate: Optional[FhirDateTime] = None,
        presentationDate: Optional[FhirDateTime] = None,
    ) -> None:
        """
        ImmunizationEducationBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/immunization-definitions.html#Immunization.education
        """
        super().__init__(
            id_=id_,
            documentType=documentType,
            reference=reference,
            publicationDate=publicationDate,
            presentationDate=presentationDate,
        )
