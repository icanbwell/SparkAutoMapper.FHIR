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
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceReferenceInformationTarget(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        target: Optional[Identifier] = None,
        type: Optional[CodeableConcept] = None,
        interaction: Optional[CodeableConcept] = None,
        organism: Optional[CodeableConcept] = None,
        organismType: Optional[CodeableConcept] = None,
        amountType: Optional[CodeableConcept] = None,
        source: Optional[FhirList[Reference[Union[DocumentReference]]]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param target: Todo.
        :param type: Todo.
        :param interaction: Todo.
        :param organism: Todo.
        :param organismType: Todo.
        :param amountType: Todo.
        :param source: Todo.
        """
        super().__init__(
            resourceType="SubstanceReferenceInformationTarget",
            id_=id_,
            meta=meta,
            extension=extension,
            target=target,
            type=type,
            interaction=interaction,
            organism=organism,
            organismType=organismType,
            amountType=amountType,
            source=source,
        )