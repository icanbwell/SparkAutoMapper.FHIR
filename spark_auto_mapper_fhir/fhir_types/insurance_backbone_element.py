from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperBooleanInputType, AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.coverage import AutoMapperFhirDataTypeCoverage
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference


class AutoMapperFhirDataTypeInsuranceBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            focal: AutoMapperBooleanInputType,
            coverage: AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypeCoverage],
            preAuthRef: Optional[AutoMapperDataTypeList[AutoMapperTextInputType]] = None
            ) -> 'AutoMapperFhirDataTypeInsuranceBackboneElement':
        """
        InsuranceBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#InsuranceBackboneElement
        Patient insurance information


        :param focal: Coverage to be used for adjudication
        :param coverage: Insurance information
        :param preAuthRef: 	Prior authorization reference number
        """
        return AutoMapperFhirDataTypeInsuranceBackboneElement(
            focal=focal,
            coverage=coverage,
            preAuthRef=preAuthRef
        )
