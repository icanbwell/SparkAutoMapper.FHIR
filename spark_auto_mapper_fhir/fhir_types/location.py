from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.identifier import AutoMapperFhirDataTypeIdentifier


class AutoMapperFhirDataTypeLocation(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            identifier: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeIdentifier]] = None,
            name: Optional[AutoMapperTextInputType] = None
            ) -> 'AutoMapperFhirDataTypeLocation':
        """
        Location Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Location


        """
        return AutoMapperFhirDataTypeLocation(
            identifier=identifier,
            name=name
        )
