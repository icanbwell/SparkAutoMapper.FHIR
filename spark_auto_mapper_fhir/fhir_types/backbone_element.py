from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept


class AutoMapperFhirDataTypeBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            type_: Optional[AutoMapperFhirDataTypeCodeableConcept] = None
            ) -> 'AutoMapperFhirDataTypeBackboneElement':
        """
        BackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#BackboneElement

        :param type_: type
        """
        return AutoMapperFhirDataTypeBackboneElement(
            type_=type_
        )
