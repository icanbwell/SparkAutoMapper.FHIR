from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class NotAvailableBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        description: FhirString,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        during: Optional[Period] = None,
    ) -> None:
        """
        NotAvailableBackboneElement Backbone Element in FHIR
        https://hl7.org/FHIR/practitionerrole-definitions.html#PractitionerRole.notAvailable
        Not available during this time due to provided reason


        :param description: Reason presented to the user explaining why time not available
        :param during: Service not available from this date
        """
        super().__init__(
            id_=id_, extension=extension, description=description, during=during
        )
