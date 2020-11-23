from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.adjudication_reason import AdjudicationReasonCode
from spark_auto_mapper_fhir.valuesets.adjudication_value import AdjudicationValueCode
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.complex_types.money import Money


class AdjudicationBackboneElement(FhirBackboneElementBase):
    # noinspection SpellCheckingInspection
    def __init__(
        self,
        category: CodeableConcept[AdjudicationValueCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        reason: Optional[CodeableConcept[AdjudicationReasonCode]] = None,
        amount: Optional[Money] = None,
        value: Optional[FhirDecimal] = None
    ):
        """
        Adjudication Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Adjudication
        Example: https://hl7.org/FHIR/explanationofbenefit-example.json.html

        :param category: Type of adjudication information. http://hl7.org/fhir/valueset-adjudication.html
        :param reason: Explanation of adjudication outcome. http://hl7.org/fhir/valueset-adjudication-reason.html
        :param amount: Monetary amount
        :param value: Non-monitary value
        """
        super().__init__(
            id_=id_,
            extension=extension,
            category=category,
            reason=reason,
            amount=amount,
            value=value
        )
