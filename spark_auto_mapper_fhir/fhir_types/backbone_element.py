from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept


class FhirBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            type_: Optional[FhirCodeableConcept] = None
            ) -> 'FhirBackboneElement':
        """
        BackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#BackboneElement

        :param type_: type
        """
        return FhirBackboneElement(
            type_=type_
        )
