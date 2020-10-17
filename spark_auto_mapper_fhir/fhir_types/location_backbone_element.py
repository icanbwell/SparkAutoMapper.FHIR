from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.address import AutoMapperFhirDataTypeAddress
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.location import AutoMapperFhirDataTypeLocation
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference


class AutoMapperFhirDataTypeLocationBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            locationCodeableConcept: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            locationAddress: Optional[AutoMapperFhirDataTypeAddress] = None,
            locationReference: Optional[AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypeLocation]] = None
            ) -> 'AutoMapperFhirDataTypeLocationBackboneElement':
        """
        LocationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit.html
        Place of service or where product was supplied
        https://hl7.org/FHIR/valueset-service-place.html

        :param locationCodeableConcept:
        :param locationAddress:
        :param locationReference:
        """
        return AutoMapperFhirDataTypeLocationBackboneElement(
            locationCodeableConcept=locationCodeableConcept,
            locationAddress=locationAddress,
            locationReference=locationReference
        )
