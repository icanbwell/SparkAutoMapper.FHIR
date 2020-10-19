from typing import Optional, Union

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.adjudication_backbone_element import FhirAdjudicationBackboneElement
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_modifiers import ClaimModifiersCode
from spark_auto_mapper_fhir.fhir_types.valuesets.ex_program import ExProgramReasonCode
from spark_auto_mapper_fhir.fhir_types.valuesets.service_place import ServicePlaceCode
from spark_auto_mapper_fhir.fhir_types.valuesets.service_uscls import ServiceUSCLSCode
from spark_auto_mapper_fhir.fhir_types.valuesets.surface import SurfaceCode
from spark_auto_mapper_fhir.fhir_types.valuesets.tooth import ToothCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.location import FhirLocation
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.simple_quantity import FhirSimpleQuantity


class FhirAddItemBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        productOrService: FhirCodeableConcept[ServiceUSCLSCode],
        itemSequence: Optional[FhirList[FhirPositiveInt]] = None,
        detailSequence: Optional[FhirList[FhirPositiveInt]] = None,
        subDetailSequence: Optional[FhirList[FhirPositiveInt]] = None,
        provider: Optional[FhirReference[Union[FhirPractitioner,
                                               FhirPractitionerRole,
                                               FhirOrganization]]] = None,
        modifier: Optional[FhirList[FhirCodeableConcept[ClaimModifiersCode]]
                           ] = None,
        programCode: Optional[FhirList[FhirCodeableConcept[ExProgramReasonCode]
                                       ]] = None,
        servicedDate: Optional[FhirDate] = None,
        servicedPeriod: Optional[FhirPeriod] = None,
        locationCodeableConcept: Optional[FhirCodeableConcept[ServicePlaceCode]
                                          ] = None,
        locationAddress: Optional[FhirAddress] = None,
        locationReference: Optional[FhirReference[FhirLocation]] = None,
        quantity: Optional[FhirSimpleQuantity] = None,
        unitPrice: Optional[FhirMoney] = None,
        factor: Optional[FhirDecimal] = None,
        net: Optional[FhirMoney] = None,
        bodySite: Optional[FhirCodeableConcept[ToothCode]] = None,
        subSite: Optional[FhirList[FhirCodeableConcept[SurfaceCode]]] = None,
        noteNumber: Optional[FhirList[FhirPositiveInt]] = None,
        adjudication: Optional[FhirList[FhirAdjudicationBackboneElement]
                               ] = None
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
            adjudication=adjudication
        )
