from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.adjudication_reason import FhirAdjudicationReasonCode
from spark_auto_mapper_fhir.fhir_types.valuesets.adjudication_value import FhirAdjudicationValueCode
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney


class FhirAdjudicationBackboneElement(FhirResourceBase):
    # noinspection SpellCheckingInspection
    @classmethod
    def map(
        cls,
        category: FhirCodeableConcept[FhirAdjudicationValueCode],
        reason: Optional[FhirCodeableConcept[FhirAdjudicationReasonCode]
                         ] = None,
        amount: Optional[FhirMoney] = None,
        value: Optional[FhirDecimal] = None
    ) -> 'FhirAdjudicationBackboneElement':
        """
        Adjudication Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Adjudication
        Example: https://hl7.org/FHIR/explanationofbenefit-example.json.html

        :param category: Type of adjudication information. http://hl7.org/fhir/valueset-adjudication.html
        :param reason: Explanation of adjudication outcome. http://hl7.org/fhir/valueset-adjudication-reason.html
        :param amount: Monetary amount
        :param value: Non-monitary value
        """
        return FhirAdjudicationBackboneElement(
            category=category, reason=reason, amount=amount, value=value
        )
