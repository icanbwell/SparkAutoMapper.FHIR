from typing import Optional, Any
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.claim_exception import ClaimExceptionCode
from spark_auto_mapper_fhir.valuesets.claim_information_category import (
    ClaimInformationCategoryCode,
)
from spark_auto_mapper_fhir.valuesets.missing_tooth_reason import MissingToothReasonCode
from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.complex_types.quantity import Quantity
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class SupportingInfoBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        sequence: FhirPositiveInt,
        category: CodeableConcept[ClaimInformationCategoryCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[CodeableConcept[ClaimExceptionCode]] = None,
        timingDate: Optional[FhirDate] = None,
        timingPeriod: Optional[Period] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueString: Optional[FhirString] = None,
        valueQuantity: Optional[Quantity] = None,
        valueAttachment: Optional[Attachment] = None,
        valueReference: Optional[Reference[Any]] = None,
        reason: Optional[Coding[MissingToothReasonCode]] = None,
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
            id_=id_,
            extension=extension,
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
            reason=reason,
        )
