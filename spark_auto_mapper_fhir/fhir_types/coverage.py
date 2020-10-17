from typing import Optional, Union

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.identifier import AutoMapperFhirDataTypeIdentifier
from spark_auto_mapper_fhir.fhir_types.organization import AutoMapperFhirDataTypeOrganization
from spark_auto_mapper_fhir.fhir_types.patient import AutoMapperFhirDataTypePatient
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference
from spark_auto_mapper_fhir.fhir_types.related_person import AutoMapperFhirDataTypeRelatedPerson


class AutoMapperFhirDataTypeCoverage(AutoMapperDataTypeComplexBase):
    # noinspection SpellCheckingInspection
    @classmethod
    def map(cls,
            payor: AutoMapperDataTypeList[
                AutoMapperFhirDataTypeReference[
                    Union[
                        AutoMapperFhirDataTypeOrganization,
                        AutoMapperFhirDataTypePatient,
                        AutoMapperFhirDataTypeRelatedPerson
                    ]
                ]
            ],
            identifier: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeIdentifier]] = None,
            dependent: Optional[AutoMapperTextInputType] = None,
            relationship: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            ) -> 'AutoMapperFhirDataTypeCoverage':
        """
        Coverage Resource in FHIR
        https://hl7.org/FHIR/coverage.html


        """
        return AutoMapperFhirDataTypeCoverage(
            payor=payor,
            identifier=identifier,
            dependent=dependent,
            relationship=relationship
        )
