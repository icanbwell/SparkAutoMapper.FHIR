from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
# noinspection SpellCheckingInspection
from spark_auto_mapper_fhir.fhir_types.period import AutoMapperFhirDataTypePeriod

from spark_auto_mapper_fhir.fhir_types.uri import AutoMapperFhirUriInputType


class AutoMapperFhirDataTypeIdentifier(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference

    @classmethod
    def map(cls,
            use: Optional[AutoMapperFhirCodeInputType] = None,
            type_: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            system: Optional[AutoMapperFhirUriInputType] = None,
            value: Optional[AutoMapperTextInputType] = None,
            period: Optional[AutoMapperFhirDataTypePeriod] = None,
            assigner: Optional['AutoMapperFhirDataTypeReference'] = None
            ) -> 'AutoMapperFhirDataTypeIdentifier':
        """
        Identifier Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Identifier
        An identifier intended for computation


        :param use: usual | official | temp | secondary | old (If known) (https://hl7.org/FHIR/valueset-identifier-use.html)
        :param type_: Description of identifier https://hl7.org/FHIR/valueset-identifier-type.html
        :param system: 	The namespace for the identifier value
        :param value: The value that is unique
        :param period: Time period when id is/was valid for use
        :param assigner: Organization that issued id (may be just text)
        """
        return AutoMapperFhirDataTypeIdentifier(
            use=use,
            type_=type_,
            system=system,
            value=value,
            period=period,
            assigner=assigner
        )
