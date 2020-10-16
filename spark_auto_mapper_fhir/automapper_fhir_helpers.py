from typing import Type

from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_human_name import AutoMapperFhirDataTypeHumanName
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_patient import AutoMapperFhirDataTypePatient


class AutoMapperFhirHelpers:
    patient: Type[AutoMapperFhirDataTypePatient] = AutoMapperFhirDataTypePatient
    human_name: Type[AutoMapperFhirDataTypeHumanName] = AutoMapperFhirDataTypeHumanName
