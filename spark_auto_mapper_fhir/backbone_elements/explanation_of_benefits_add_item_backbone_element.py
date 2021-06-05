from typing import Optional, Union

from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefits_add_item_detail_backbone_element import (
    ExplanationOfBenefitsAddItemDetailBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.adjudication_backbone_element import (
    AdjudicationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.money import Money
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.valuesets.claim_modifiers import ClaimModifiersCode
from spark_auto_mapper_fhir.valuesets.ex_program import ExProgramReasonCode
from spark_auto_mapper_fhir.valuesets.service_place import ServicePlaceCode
from spark_auto_mapper_fhir.valuesets.service_uscls import ServiceUSCLSCode
from spark_auto_mapper_fhir.valuesets.surface import SurfaceCode
from spark_auto_mapper_fhir.valuesets.tooth import ToothCode


class ExplanationOfBenefitsAddItemBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        productOrService: CodeableConcept[ServiceUSCLSCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        itemSequence: Optional[FhirList[FhirPositiveInt]] = None,
        detailSequence: Optional[FhirList[FhirPositiveInt]] = None,
        subDetailSequence: Optional[FhirList[FhirPositiveInt]] = None,
        provider: Optional[
            FhirList[Reference[Union[Practitioner, PractitionerRole, Organization]]]
        ] = None,
        modifier: Optional[FhirList[CodeableConcept[ClaimModifiersCode]]] = None,
        programCode: Optional[FhirList[CodeableConcept[ExProgramReasonCode]]] = None,
        servicedDate: Optional[FhirDate] = None,
        servicedPeriod: Optional[Period] = None,
        locationCodeableConcept: Optional[CodeableConcept[ServicePlaceCode]] = None,
        locationAddress: Optional[Address] = None,
        locationReference: Optional[Reference[Location]] = None,
        quantity: Optional[SimpleQuantity] = None,
        unitPrice: Optional[Money] = None,
        factor: Optional[FhirDecimal] = None,
        net: Optional[Money] = None,
        bodySite: Optional[CodeableConcept[ToothCode]] = None,
        subSite: Optional[FhirList[CodeableConcept[SurfaceCode]]] = None,
        noteNumber: Optional[FhirList[FhirPositiveInt]] = None,
        adjudication: Optional[FhirList[AdjudicationBackboneElement]] = None,
        detail: Optional[
            FhirList[ExplanationOfBenefitsAddItemDetailBackboneElement]
        ] = None,
    ):
        """
        AddItemBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.addItem
        Insurer added line items

        :param productOrService: Billing, service, product, or drug code.  https://hl7.org/FHIR/valueset-service-uscls.html
        :param itemSequence: Item sequence number
        :param detailSequence: Detail sequence number
        :param subDetailSequence: SubDetail seuqence number
        :param provider: Authorized providers
        :param modifier: Service/Product billing modifiers. https://hl7.org/FHIR/valueset-claim-modifiers.html
        :param programCode: Program the product or service is provided under. https://hl7.org/FHIR/valueset-ex-program-code.html
        :param servicedDate: Date or dates of service or product delivery
        :param servicedPeriod: Date or dates of service or product delivery
        :param locationCodeableConcept: Place of service or where product was supplied. https://hl7.org/FHIR/valueset-service-place.html
        :param locationAddress: Place of service or where product was supplied.
        :param locationReference: Place of service or where product was supplied.
        :param quantity: Count of products or services
        :param unitPrice: Fee, charge or cost per item
        :param factor: Price scaling factor
        :param net: Total item cost
        :param bodySite: Anatomical location. https://hl7.org/FHIR/valueset-tooth.html
        :param subSite: Anatomical sub-location. https://hl7.org/FHIR/valueset-surface.html
        :param noteNumber: Applicable note numbers
        :param adjudication: Added items adjudication
        """
        super().__init__(
            id_=id_,
            extension=extension,
            productOrService=productOrService,
            itemSequence=itemSequence,
            detailSequence=detailSequence,
            subDetailSequence=subDetailSequence,
            provider=provider,
            modifier=modifier,
            programCode=programCode,
            servicedDate=servicedDate,
            servicedPeriod=servicedPeriod,
            locationCodeableConcept=locationCodeableConcept,
            locationAddress=locationAddress,
            locationReference=locationReference,
            quantity=quantity,
            unitPrice=unitPrice,
            factor=factor,
            net=net,
            bodySite=bodySite,
            subSite=subSite,
            noteNumber=noteNumber,
            adjudication=adjudication,
            detail=detail,
        )
