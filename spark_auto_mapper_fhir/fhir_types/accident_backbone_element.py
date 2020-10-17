from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.address import AutoMapperFhirDataTypeAddress
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.location import AutoMapperFhirDataTypeLocation
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference


class FhirAccidentBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            date: Optional[FhirDate] = None,
            type_: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            locationAddress: Optional[AutoMapperFhirDataTypeAddress] = None,
            locationReference: Optional[AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypeLocation]] = None
            ) -> 'FhirAccidentBackboneElement':
        """
        AccidentBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.accident
        Details of the event

        :param date: When the incident occurred
        :param type_: The nature of the accident.  https://hl7.org/FHIR/v3/ActIncidentCode/vs.html
        :param locationAddress: Where the event occurred
        :param locationReference: Where the event occurred
        """
        return FhirAccidentBackboneElement(
            date=date,
            type_=type_,
            locationAddress=locationAddress,
            locationReference=locationReference
        )
