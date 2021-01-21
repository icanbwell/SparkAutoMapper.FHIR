from typing import Optional, Union
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase


class GroupMemberBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        entity: Optional[Reference[Union[Patient, Practitioner,
                                         PractitionerRole, Device]]] = None,
        period: Optional[Period] = None,
        inactive: Optional[FhirBoolean] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            entity=entity,
            period=period,
            inactive=inactive
        )
