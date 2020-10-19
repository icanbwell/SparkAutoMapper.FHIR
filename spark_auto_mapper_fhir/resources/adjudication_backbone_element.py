from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.adjudication_reason import AdjudicationReasonCode
from spark_auto_mapper_fhir.valuesets.adjudication_value import AdjudicationValueCode
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.resources.money import Money


class AdjudicationBackboneElement(FhirResourceBase):
    # noinspection SpellCheckingInspection
    def __init__(
        self,
        category: CodeableConcept[AdjudicationValueCode],
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
            category=category, reason=reason, amount=amount, value=value
        )
