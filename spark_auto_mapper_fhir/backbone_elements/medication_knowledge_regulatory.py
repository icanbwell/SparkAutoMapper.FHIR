from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for regulatoryAuthority
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_substitution import (
        MedicationKnowledgeSubstitution,
    )
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_schedule import (
        MedicationKnowledgeSchedule,
    )
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_max_dispense import (
        MedicationKnowledgeMaxDispense,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationKnowledgeRegulatory(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        regulatoryAuthority: Reference[Union[Organization]],
        substitution: Optional[FhirList[MedicationKnowledgeSubstitution]] = None,
        schedule: Optional[FhirList[MedicationKnowledgeSchedule]] = None,
        maxDispense: Optional[MedicationKnowledgeMaxDispense] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param regulatoryAuthority: The authority that is specifying the regulations.
            :param substitution: Specifies if changes are allowed when dispensing a medication from a
        regulatory perspective.
            :param schedule: Specifies the schedule of a medication in jurisdiction.
            :param maxDispense: The maximum number of units of the medication that can be dispensed in a
        period.
        """
        super().__init__(
            resourceType="MedicationKnowledgeRegulatory",
            id_=id_,
            meta=meta,
            extension=extension,
            regulatoryAuthority=regulatoryAuthority,
            substitution=substitution,
            schedule=schedule,
            maxDispense=maxDispense,
        )