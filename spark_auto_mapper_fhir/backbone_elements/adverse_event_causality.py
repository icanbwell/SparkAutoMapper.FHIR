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
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for author
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AdverseEventCausality(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        assessment: Optional[CodeableConcept] = None,
        productRelatedness: Optional[string] = None,
        author: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        method: Optional[CodeableConcept] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param assessment: Assessment of if the entity caused the event.
        :param productRelatedness: AdverseEvent.suspectEntity.causalityProductRelatedness.
        :param author: AdverseEvent.suspectEntity.causalityAuthor.
        :param method: ProbabilityScale | Bayesian | Checklist.
        """
        super().__init__(
            resourceType="AdverseEventCausality",
            id_=id_,
            meta=meta,
            extension=extension,
            assessment=assessment,
            productRelatedness=productRelatedness,
            author=author,
            method=method,
        )