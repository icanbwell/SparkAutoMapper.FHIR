from typing import Optional

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_human_name import AutoMapperFhirDataTypeHumanName
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_patient import AutoMapperFhirDataTypePatient


class AutoMapperFhirHelpers:
    # noinspection PyPep8Naming
    @staticmethod
    def patient(id_: AutoMapperTextInputType,
                birthDate: AutoMapperDateDataType,
                name: AutoMapperDataTypeList,
                gender: AutoMapperTextInputType
                ) -> AutoMapperFhirDataTypePatient:
        """
        Patient Resource in FHIR
        https://hl7.org/FHIR/patient.html


        :param id_: id of resource
        :param birthDate: The date of birth for the individual
        :param name: A name associated with the patient
        :param gender: 	male | female | other | unknown (https://hl7.org/FHIR/valueset-administrative-gender.html)
        """
        return AutoMapperFhirDataTypePatient(
            id_=id_,
            birthDate=birthDate,
            name=name,
            gender=gender
        )

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
