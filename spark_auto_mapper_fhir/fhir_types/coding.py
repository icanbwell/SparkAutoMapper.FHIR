from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType, AutoMapperBooleanInputType

from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.uri import AutoMapperFhirUriInputType


class AutoMapperFhirDataTypeCoding(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            system: Optional[AutoMapperFhirUriInputType] = None,
            version: Optional[AutoMapperTextInputType] = None,
            code: Optional[AutoMapperFhirCodeInputType] = None,
            display: Optional[AutoMapperTextInputType] = None,
            userSelected: Optional[AutoMapperBooleanInputType] = None
            ) -> 'AutoMapperFhirDataTypeCoding':
        """
        Coding Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Coding


        :param system: Identity of the terminology system
        :param version: Version of the system - if relevant
        :param code: 	Symbol in syntax defined by the system
        :param display: Representation defined by the system
        :param userSelected: If this coding was chosen directly by the user
        """
        return AutoMapperFhirDataTypeCoding(
            system=system,
            version=version,
            code=code,
            display=display,
            userSelected=userSelected
        )
