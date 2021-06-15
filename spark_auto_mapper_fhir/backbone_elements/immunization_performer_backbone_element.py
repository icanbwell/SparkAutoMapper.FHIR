from typing import Optional, Union

from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.valuesets.immunization_function import (
    ImmunizationFunctionCode,
)


class ImmunizationPerformerBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        function: Optional[FhirList[FhirList[ImmunizationFunctionCode]]] = None,
        actor: Reference[
            Union[
                Practitioner,
                PractitionerRole,
                Organization,
            ]
        ],
    ) -> None:
        """
        ImmunizationFunctionCode Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        http://hl7.org/fhir/ValueSet/immunization-function
        """
        super().__init__(id_=id_, function=function, actor=actor)
