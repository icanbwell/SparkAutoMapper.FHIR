from typing import Optional, Any

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.attachment import FhirAttachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_exception import FhirClaimExceptionCode
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_information_category import FhirClaimInformationCategoryCode
from spark_auto_mapper_fhir.fhir_types.valuesets.missing_tooth_reason import FhirMissingToothReasonCode
from spark_auto_mapper_fhir.fhir_types.coding import FhirCoding
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.quantity import FhirQuantity
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirSupportingInfoBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        sequence: FhirPositiveInt,
        category: FhirCodeableConcept[FhirClaimInformationCategoryCode],
        code: Optional[FhirCodeableConcept[FhirClaimExceptionCode]] = None,
        timingDate: Optional[FhirDate] = None,
        timingPeriod: Optional[FhirPeriod] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueString: Optional[FhirString] = None,
        valueQuantity: Optional[FhirQuantity] = None,
        valueAttachment: Optional[FhirAttachment] = None,
        valueReference: Optional[FhirReference[Any]] = None,
        reason: Optional[FhirCoding[FhirMissingToothReasonCode]] = None
    ) -> 'FhirSupportingInfoBackboneElement':
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
        return FhirSupportingInfoBackboneElement(
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
