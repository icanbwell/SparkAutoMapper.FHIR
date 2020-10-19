from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.adjudication_backbone_element import FhirAdjudicationBackboneElement
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_modifiers import FhirClaimModifiersCode
from spark_auto_mapper_fhir.fhir_types.valuesets.ex_revenue_center import FhirExRevenueCenterCode
from spark_auto_mapper_fhir.fhir_types.valuesets.service_place import FhirServicePlaceCode
from spark_auto_mapper_fhir.fhir_types.valuesets.service_uscls import FhirServiceUSCLSCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.location import FhirLocation
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.simple_quantity import FhirSimpleQuantity


class FhirRevenueItemBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(
        cls,
        sequence: FhirPositiveInt,
        productOrService: FhirList[FhirCodeableConcept[FhirServiceUSCLSCode]],
        informationSequence: Optional[FhirList[FhirPositiveInt]] = None,
        revenue: Optional[FhirList[FhirCodeableConcept[FhirExRevenueCenterCode]
                                   ]] = None,
        modifier: Optional[FhirList[FhirCodeableConcept[FhirClaimModifiersCode]
                                    ]] = None,
        quantity: Optional[FhirList[FhirSimpleQuantity]] = None,
        factor: Optional[FhirDecimal] = None,
        adjudication: Optional[FhirList[FhirAdjudicationBackboneElement]
                               ] = None,
        servicedDate: Optional[FhirDate] = None,
        servicedPeriod: Optional[FhirPeriod] = None,
        locationCodeableConcept: Optional[
            FhirCodeableConcept[FhirServicePlaceCode]] = None,
        locationAddress: Optional[FhirAddress] = None,
        locationReference: Optional[FhirReference[FhirLocation]] = None
    ) -> 'FhirRevenueItemBackboneElement':
        """
        RevenueItemBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.item
        Product or service provided

        :param sequence: Item instance identifier
        :param informationSequence: Applicable exception and supporting information
        :param productOrService: Billing, service, product, or drug code. https://hl7.org/FHIR/valueset-service-uscls.html
        :param revenue: Revenue or cost center code. https://hl7.org/FHIR/valueset-ex-revenue-center.html
        :param modifier: Product or service billing modifiers. https://hl7.org/FHIR/valueset-claim-modifiers.html
        :param quantity: Count of products or services
        :param factor: Price scaling factor
        :param adjudication: Added items adjudication.
                            https://hl7.org/FHIR/explanationofbenefit.html#ExplanationOfBenefit.item.adjudication
        :param servicedDate: Date or dates of service or product delivery
        :param servicedPeriod: Date or dates of service or product delivery
        :param locationCodeableConcept: Place of service or where product was supplied. https://hl7.org/FHIR/valueset-service-place.html
        :param locationAddress: Place of service or where product was supplied.
        :param locationReference: Place of service or where product was supplied.
        """
        return FhirRevenueItemBackboneElement(
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
            locationReference=locationReference
        )
