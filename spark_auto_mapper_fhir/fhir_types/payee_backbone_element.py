from typing import Optional, Union

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_patient import AutoMapperFhirDataTypePatient

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.organization import AutoMapperFhirDataTypeOrganization
from spark_auto_mapper_fhir.fhir_types.practitioner import AutoMapperFhirDataTypePractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import AutoMapperFhirDataTypePractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference
from spark_auto_mapper_fhir.fhir_types.related_person import AutoMapperFhirDataTypeRelatedPerson


class AutoMapperFhirDataTypePayeeBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            type_: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            party: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypePractitioner,
                    AutoMapperFhirDataTypePractitionerRole,
                    AutoMapperFhirDataTypeOrganization,
                    AutoMapperFhirDataTypePatient,
                    AutoMapperFhirDataTypeRelatedPerson
                ]
            ]] = None
            ) -> 'AutoMapperFhirDataTypePayeeBackboneElement':
        """
        PayeeBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#PayeeBackboneElement


        :param type_: Category of recipient https://hl7.org/FHIR/valueset-payeetype.html
        :param party: Recipient reference
        """
        return AutoMapperFhirDataTypePayeeBackboneElement(
            type_=type_,
            party=party
        )
