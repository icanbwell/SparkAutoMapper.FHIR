from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity
    from spark_auto_mapper_fhir.complex_types.money import Money
    from spark_auto_mapper_fhir.complex_types.decimal import decimal
    from spark_auto_mapper_fhir.complex_types.money import Money
    from spark_auto_mapper_fhir.complex_types.positive_int import positiveInt
    from spark_auto_mapper_fhir.backbone_elements.claim_response_adjudication import (
        ClaimResponseAdjudication,
    )
    from spark_auto_mapper_fhir.backbone_elements.claim_response_sub_detail1 import (
        ClaimResponseSubDetail1,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimResponseDetail1(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        productOrService: CodeableConcept,
        modifier: Optional[FhirList[CodeableConcept]] = None,
        quantity: Optional[Quantity] = None,
        unitPrice: Optional[Money] = None,
        factor: Optional[decimal] = None,
        net: Optional[Money] = None,
        noteNumber: Optional[FhirList[positiveInt]] = None,
        adjudication: FhirList[ClaimResponseAdjudication],
        subDetail: Optional[FhirList[ClaimResponseSubDetail1]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param productOrService: When the value is a group code then this item collects a set of related claim
        details, otherwise this contains the product, service, drug or other billing
        code for the item.
            :param modifier: Item typification or modifiers codes to convey additional context for the
        product or service.
            :param quantity: The number of repetitions of a service or product.
            :param unitPrice: If the item is not a group then this is the fee for the product or service,
        otherwise this is the total of the fees for the details of the group.
            :param factor: A real number that represents a multiplier used in determining the overall
        value of services delivered and/or goods received. The concept of a Factor
        allows for a discount or surcharge multiplier to be applied to a monetary
        amount.
            :param net: The quantity times the unit price for an additional service or product or
        charge.
            :param noteNumber: The numbers associated with notes below which apply to the adjudication of
        this item.
            :param adjudication: The adjudication results.
            :param subDetail: The third-tier service adjudications for payor added services.
        """
        super().__init__(
            resourceType="ClaimResponseDetail1",
            id_=id_,
            meta=meta,
            extension=extension,
            productOrService=productOrService,
            modifier=modifier,
            quantity=quantity,
            unitPrice=unitPrice,
            factor=factor,
            net=net,
            noteNumber=noteNumber,
            adjudication=adjudication,
            subDetail=subDetail,
        )