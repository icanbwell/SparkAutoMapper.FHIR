from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperBooleanInputType, AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.coverage import FhirCoverage
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class FhirInsuranceBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            focal: AutoMapperBooleanInputType,
            coverage: FhirReference[FhirCoverage],
            preAuthRef: Optional[AutoMapperDataTypeList[AutoMapperTextInputType]] = None
            ) -> 'FhirInsuranceBackboneElement':
        """
        InsuranceBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#InsuranceBackboneElement
        Patient insurance information


        :param focal: Coverage to be used for adjudication
        :param coverage: Insurance information
        :param preAuthRef: 	Prior authorization reference number
        """
        return FhirInsuranceBackboneElement(
            focal=focal,
            coverage=coverage,
            preAuthRef=preAuthRef
        )
