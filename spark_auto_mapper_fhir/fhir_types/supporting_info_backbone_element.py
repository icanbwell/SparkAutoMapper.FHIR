from typing import Optional, Union

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType, AutoMapperBooleanInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.coding import AutoMapperFhirDataTypeCoding
from spark_auto_mapper_fhir.fhir_types.positive_int import AutoMapperFhirPositiveIntInputType
from spark_auto_mapper_fhir.fhir_types.simple_quantity import AutoMapperFhirDataTypeSimpleQuantity
from spark_auto_mapper_fhir.fhir_types.timing_date_or_period import AutoMapperFhirDataTypeTimingDateOrPeriod


class AutoMapperFhirDataTypeSupportingInfoBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            sequence: AutoMapperFhirPositiveIntInputType,
            category: AutoMapperFhirDataTypeCodeableConcept,
            code: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            timing: Optional[AutoMapperFhirDataTypeTimingDateOrPeriod] = None,
            value: Optional[Union[
                AutoMapperTextInputType,
                AutoMapperBooleanInputType,
                AutoMapperFhirDataTypeSimpleQuantity
            ]] = None,
            reason: Optional[AutoMapperFhirDataTypeCoding] = None
            ) -> 'AutoMapperFhirDataTypeSupportingInfoBackboneElement':
        """
        SupportingInfoBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SupportingInfoBackboneElement
        """
        return AutoMapperFhirDataTypeSupportingInfoBackboneElement(
            sequence=sequence,
            category=category,
            code=code,
            timing=timing,
            value=value,
            reason=reason
        )
