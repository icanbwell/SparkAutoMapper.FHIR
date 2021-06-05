from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefits_add_item_sub_detail_backbone_element import (
    ExplanationOfBenefitsAddItemSubDetailBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.adjudication_backbone_element import (
    AdjudicationBackboneElement,
)
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.money import Money
from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.valuesets.claim_modifiers import ClaimModifiersCode
from spark_auto_mapper_fhir.valuesets.service_uscls import ServiceUSCLSCode


class ExplanationOfBenefitsAddItemDetailBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        productOrService: CodeableConcept[ServiceUSCLSCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifier: Optional[FhirList[CodeableConcept[ClaimModifiersCode]]] = None,
        quantity: Optional[SimpleQuantity] = None,
        unitPrice: Optional[Money] = None,
        factor: Optional[FhirDecimal] = None,
        net: Optional[Money] = None,
        noteNumber: Optional[FhirList[FhirPositiveInt]] = None,
        adjudication: Optional[FhirList[AdjudicationBackboneElement]] = None,
        subDetail: Optional[
            FhirList[ExplanationOfBenefitsAddItemSubDetailBackboneElement]
        ] = None,
    ) -> None:
        """
        AddItemDetailBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
         properties not just the ones you need
        https://www.hl7.org/fhir/explanationofbenefit-definitions.html#ExplanationOfBenefit.addItem.detail
        """
        super().__init__(
            id_=id_,
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
