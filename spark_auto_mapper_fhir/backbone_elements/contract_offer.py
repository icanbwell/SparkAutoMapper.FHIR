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
    from spark_auto_mapper_fhir.backbone_elements.contract_party import ContractParty
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for topic
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.backbone_elements.contract_answer import ContractAnswer
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.unsigned_int import unsignedInt


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractOffer(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        party: Optional[FhirList[ContractParty]] = None,
        topic: Optional[Reference[Union[Resource]]] = None,
        type: Optional[CodeableConcept] = None,
        decision: Optional[CodeableConcept] = None,
        decisionMode: Optional[FhirList[CodeableConcept]] = None,
        answer: Optional[FhirList[ContractAnswer]] = None,
        text: Optional[string] = None,
        linkId: Optional[FhirList[string]] = None,
        securityLabelNumber: Optional[FhirList[unsignedInt]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Unique identifier for this particular Contract Provision.
            :param party: Offer Recipient.
            :param topic: The owner of an asset has the residual control rights over the asset: the
        right to decide all usages of the asset in any way not inconsistent with a
        prior contract, custom, or law (Hart, 1995, p. 30).
            :param type: Type of Contract Provision such as specific requirements, purposes for
        actions, obligations, prohibitions, e.g. life time maximum benefit.
            :param decision: Type of choice made by accepting party with respect to an offer made by an
        offeror/ grantee.
            :param decisionMode: How the decision about a Contract was conveyed.
            :param answer: Response to offer text.
            :param text: Human readable form of this Contract Offer.
            :param linkId: The id of the clause or question text of the offer in the referenced
        questionnaire/response.
            :param securityLabelNumber: Security labels that protects the offer.
        """
        super().__init__(
            resourceType="ContractOffer",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            party=party,
            topic=topic,
            type=type,
            decision=decision,
            decisionMode=decisionMode,
            answer=answer,
            text=text,
            linkId=linkId,
            securityLabelNumber=securityLabelNumber,
        )