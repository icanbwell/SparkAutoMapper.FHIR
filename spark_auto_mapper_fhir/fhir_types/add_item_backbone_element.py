from typing import Optional, Union

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.address import AutoMapperFhirDataTypeAddress
from spark_auto_mapper_fhir.fhir_types.adjudication import AutoMapperFhirDataTypeAdjudication
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.location import AutoMapperFhirDataTypeLocation
from spark_auto_mapper_fhir.fhir_types.money import AutoMapperFhirDataTypeMoney
from spark_auto_mapper_fhir.fhir_types.organization import AutoMapperFhirDataTypeOrganization
from spark_auto_mapper_fhir.fhir_types.period import AutoMapperFhirDataTypePeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import AutoMapperFhirPositiveIntInputType
from spark_auto_mapper_fhir.fhir_types.practitioner import AutoMapperFhirDataTypePractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import AutoMapperFhirDataTypePractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference
from spark_auto_mapper_fhir.fhir_types.simple_quantity import AutoMapperFhirDataTypeSimpleQuantity


class FhirAddItemBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            productOrService: AutoMapperFhirDataTypeCodeableConcept,
            itemSequence: Optional[FhirList[AutoMapperFhirPositiveIntInputType]] = None,
            detailSequence: Optional[FhirList[AutoMapperFhirPositiveIntInputType]] = None,
            subDetailSequence: Optional[FhirList[AutoMapperFhirPositiveIntInputType]] = None,
            provider: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypePractitioner,
                    AutoMapperFhirDataTypePractitionerRole,
                    AutoMapperFhirDataTypeOrganization
                ]
            ]] = None,
            modifier: Optional[FhirList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            programCode: Optional[FhirList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            servicedDate: Optional[FhirDate] = None,
            servicedPeriod: Optional[AutoMapperFhirDataTypePeriod] = None,
            locationCodeableConcept: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            locationAddress: Optional[AutoMapperFhirDataTypeAddress] = None,
            locationReference: Optional[AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypeLocation]] = None,
            quantity: Optional[AutoMapperFhirDataTypeSimpleQuantity] = None,
            unitPrice: Optional[AutoMapperFhirDataTypeMoney] = None,
            factor: Optional[FhirDecimal] = None,
            net: Optional[AutoMapperFhirDataTypeMoney] = None,
            bodySite: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            subSite: Optional[FhirList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            noteNumber: Optional[FhirList[AutoMapperFhirPositiveIntInputType]] = None,
            adjudication: Optional[FhirList[AutoMapperFhirDataTypeAdjudication]] = None
            ) -> 'FhirAddItemBackboneElement':
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
        return FhirAddItemBackboneElement(
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
