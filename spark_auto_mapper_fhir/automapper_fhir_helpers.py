from typing import Optional, Type

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_human_name import AutoMapperFhirDataTypeHumanName
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_patient import AutoMapperFhirDataTypePatient


class AutoMapperFhirHelpers:
    patient: Type[AutoMapperFhirDataTypePatient] = AutoMapperFhirDataTypePatient

    @staticmethod
    def human_name(
            use: Optional[AutoMapperTextInputType] = None,
            text: Optional[AutoMapperTextInputType] = None,
            family: Optional[AutoMapperTextInputType] = None
    ) -> AutoMapperFhirDataTypeHumanName:
        """
        HumanName Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#HumanName


        :param use: usual | official | temp | nickname | anonymous | old | maiden (https://hl7.org/FHIR/valueset-name-use.html)
        :param text: Text representation of the full name
        :param family: Family name (often called 'Surname')
        """
        return AutoMapperFhirDataTypeHumanName(
            use=use,
            text=text,
            family=family
        )
