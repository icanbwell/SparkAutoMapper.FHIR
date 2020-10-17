from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperNumberInputType, AutoMapperAmountInputType, \
    AutoMapperDateInputType

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.adjudication import FhirAdjudication
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.location import FhirLocation
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.simple_quantity import FhirSimpleQuantity


class FhirRevenueItemBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            sequence: AutoMapperNumberInputType,
            productOrService: AutoMapperDataTypeList[FhirCodeableConcept],
            informationSequence: Optional[AutoMapperDataTypeList[FhirPositiveInt]] = None,
            revenue: Optional[AutoMapperDataTypeList[FhirCodeableConcept]] = None,
            modifier: Optional[AutoMapperDataTypeList[FhirCodeableConcept]] = None,
            quantity: Optional[AutoMapperDataTypeList[FhirSimpleQuantity]] = None,
            factor: Optional[AutoMapperAmountInputType] = None,
            adjudication: Optional[AutoMapperDataTypeList[FhirAdjudication]] = None,
            servicedDate: Optional[AutoMapperDateInputType] = None,
            servicedPeriod: Optional[FhirPeriod] = None,
            locationCodeableConcept: Optional[FhirCodeableConcept] = None,
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
        :param adjudication: Added items adjudication. https://hl7.org/FHIR/explanationofbenefit.html#ExplanationOfBenefit.item.adjudication
        :param servicedDate: Date or dates of service or product delivery
        :param servicedPeriod: Date or dates of service or product delivery
        :param locationCodeableConcept: Place of service or where product was supplied. https://hl7.org/FHIR/valueset-service-place.html
        :param locationAddress: Place of service or where product was supplied. https://hl7.org/FHIR/valueset-service-place.html
        :param locationReference: Place of service or where product was supplied. https://hl7.org/FHIR/valueset-service-place.html
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
