from typing import Optional, Union

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.related_person import FhirRelatedPerson


class FhirCoverage(AutoMapperDataTypeComplexBase):
    # noinspection SpellCheckingInspection
    @classmethod
    def map(cls,
            payor: AutoMapperDataTypeList[
                FhirReference[
                    Union[
                        FhirOrganization,
                        FhirPatient,
                        FhirRelatedPerson
                    ]
                ]
            ],
            identifier: Optional[AutoMapperDataTypeList[FhirIdentifier]] = None,
            dependent: Optional[AutoMapperTextInputType] = None,
            relationship: Optional[FhirCodeableConcept] = None,
            ) -> 'FhirCoverage':
        """
        Coverage Resource in FHIR
        https://hl7.org/FHIR/coverage.html


        """
        return FhirCoverage(
            payor=payor,
            identifier=identifier,
            dependent=dependent,
            relationship=relationship
        )
