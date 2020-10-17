from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperNumberInputType, AutoMapperAmountInputType

from spark_auto_mapper_fhir.fhir_types.adjudication import AutoMapperFhirDataTypeAdjudication
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.location_backbone_element import AutoMapperFhirDataTypeLocationBackboneElement
from spark_auto_mapper_fhir.fhir_types.positive_int import AutoMapperFhirPositiveIntInputType
from spark_auto_mapper_fhir.fhir_types.service_date_or_period import AutoMapperFhirDataTypeServiceDateOrPeriod
from spark_auto_mapper_fhir.fhir_types.simple_quantity import AutoMapperFhirDataTypeSimpleQuantity


class AutoMapperFhirDataTypeRevenueItemBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            sequence: AutoMapperNumberInputType,
            productOrService: AutoMapperDataTypeList[AutoMapperFhirDataTypeCodeableConcept],
            informationSequence: Optional[AutoMapperDataTypeList[AutoMapperFhirPositiveIntInputType]] = None,
            revenue: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            modifier: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            quantity: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeSimpleQuantity]] = None,
            factor: Optional[AutoMapperAmountInputType] = None,
            adjudication: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeAdjudication]] = None,
            serviced: Optional[AutoMapperFhirDataTypeServiceDateOrPeriod] = None,
            location: Optional[AutoMapperFhirDataTypeLocationBackboneElement] = None
            ) -> 'AutoMapperFhirDataTypeRevenueItemBackboneElement':
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
        :param serviced: Date or dates of service or product delivery
        :param location: Place of service or where product was supplied. https://hl7.org/FHIR/valueset-service-place.html
        """
        return AutoMapperFhirDataTypeRevenueItemBackboneElement(
            sequence=sequence,
            informationSequence=informationSequence,
            productOrService=productOrService,
            revenue=revenue,
            modifier=modifier,
            quantity=quantity,
            factor=factor,
            adjudication=adjudication,
            serviced=serviced,
            location=location
        )
