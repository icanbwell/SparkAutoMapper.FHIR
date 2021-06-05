from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.adjudication_backbone_element import (
    AdjudicationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
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
from spark_auto_mapper_fhir.valuesets.claim_modifiers import ClaimModifiersCode
from spark_auto_mapper_fhir.valuesets.ex_revenue_center import ExRevenueCenterCode
from spark_auto_mapper_fhir.valuesets.service_place import ServicePlaceCode
from spark_auto_mapper_fhir.valuesets.service_uscls import ServiceUSCLSCode


class RevenueItemBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        sequence: FhirPositiveInt,
        productOrService: CodeableConcept[ServiceUSCLSCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        informationSequence: Optional[FhirList[FhirPositiveInt]] = None,
        revenue: Optional[FhirList[CodeableConcept[ExRevenueCenterCode]]] = None,
        modifier: Optional[FhirList[CodeableConcept[ClaimModifiersCode]]] = None,
        quantity: Optional[FhirList[SimpleQuantity]] = None,
        factor: Optional[FhirDecimal] = None,
        adjudication: Optional[FhirList[AdjudicationBackboneElement]] = None,
        servicedDate: Optional[FhirDate] = None,
        servicedPeriod: Optional[Period] = None,
        locationCodeableConcept: Optional[CodeableConcept[ServicePlaceCode]] = None,
        locationAddress: Optional[Address] = None,
        locationReference: Optional[Reference[Location]] = None,
    ):
        """
        RevenueItemBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.item
        Product or service provided

        :param sequence: Item instance identifier
        :param informationSequence: Applicable exception and supporting information
        :param productOrService: Billing, service, product, or drug code.
                                    https://hl7.org/FHIR/valueset-service-uscls.html
        :param revenue: Revenue or cost center code. https://hl7.org/FHIR/valueset-ex-revenue-center.html
        :param modifier: Product or service billing modifiers. https://hl7.org/FHIR/valueset-claim-modifiers.html
        :param quantity: Count of products or services
        :param factor: Price scaling factor
        :param adjudication: Added items adjudication.
                            https://hl7.org/FHIR/explanationofbenefit.html#ExplanationOfBenefit.item.adjudication
        :param servicedDate: Date or dates of service or product delivery
        :param servicedPeriod: Date or dates of service or product delivery
        :param locationCodeableConcept: Place of service or where product was supplied.
                                        https://hl7.org/FHIR/valueset-service-place.html
        :param locationAddress: Place of service or where product was supplied.
        :param locationReference: Place of service or where product was supplied.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            informationSequence=informationSequence,
            productOrService=productOrService,
            revenue=revenue,
            modifier=modifier,
            quantity=quantity,
            factor=factor,
            adjudication=adjudication,
            servicedDate=servicedDate,
            servicedPeriod=servicedPeriod,
            locationCodeableConcept=locationCodeableConcept,
            locationAddress=locationAddress,
            locationReference=locationReference,
        )
