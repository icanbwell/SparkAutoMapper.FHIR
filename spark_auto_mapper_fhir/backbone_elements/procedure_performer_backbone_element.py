from typing import Optional, Union

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.valuesets.snomed import SnoMedCode


class ProcedurePerformerBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        function: Optional[CodeableConcept[SnoMedCode]] = None,
        actor: Reference[
            Union[
                Practitioner,
                PractitionerRole,
                Organization,
                Patient,
                RelatedPerson,
                Device,
            ]
        ],
        onBehalfOf: Optional[Reference[Organization]] = None,
    ) -> None:
        """
        ProcedurePerformerBackboneElement Backbone Element in FHIR
        https://hl7.org/FHIR/procedure-definitions.html#Procedure.performer
        Limited to "real" people rather than equipment.

        :param function: Type of performance
        :param actor: The reference to the practitioner
        :param onBehalfOf: Organization the device or practitioner was acting for
        """
        super().__init__(id_=id_, function=function, actor=actor, onBehalfOf=onBehalfOf)
