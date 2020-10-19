from typing import Optional, Any

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.attachment import Attachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.claim_exception import ClaimExceptionCode
from spark_auto_mapper_fhir.valuesets.claim_information_category import ClaimInformationCategoryCode
from spark_auto_mapper_fhir.valuesets.missing_tooth_reason import MissingToothReasonCode
from spark_auto_mapper_fhir.resources.coding import Coding
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.resources.period import Period
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.resources.quantity import Quantity
from spark_auto_mapper_fhir.resources.reference import Reference
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class SupportingInfoBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        sequence: FhirPositiveInt,
        category: CodeableConcept[ClaimInformationCategoryCode],
        code: Optional[CodeableConcept[ClaimExceptionCode]] = None,
        timingDate: Optional[FhirDate] = None,
        timingPeriod: Optional[Period] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueString: Optional[FhirString] = None,
        valueQuantity: Optional[Quantity] = None,
        valueAttachment: Optional[Attachment] = None,
        valueReference: Optional[Reference[Any]] = None,
        reason: Optional[Coding[MissingToothReasonCode]] = None
    ):
        """
        SupportingInfoBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.supportingInfo


        :param sequence: Information instance identifier
        :param category: Classification of the supplied information. https://hl7.org/FHIR/valueset-claim-informationcategory.html
        :param code: Type of information. https://hl7.org/FHIR/valueset-claim-exception.html
        :param timingDate: When it occurred
        :param timingPeriod: When it occurred
        :param valueBoolean: Data to be provided
        :param valueString: Data to be provided
        :param valueQuantity: Data to be provided
        :param valueAttachment: Data to be provided
        :param valueReference: Data to be provided
        :param reason: Explanation for the information. https://hl7.org/FHIR/valueset-missing-tooth-reason.html
        """
        super().__init__(
            sequence=sequence,
            category=category,
            code=code,
            timingDate=timingDate,
            timingPeriod=timingPeriod,
            valueBoolean=valueBoolean,
            valueString=valueString,
            valueQuantity=valueQuantity,
            valueAttachment=valueAttachment,
            valueReference=valueReference,
            reason=reason
        )
