from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.familymemberhistory import (
    FamilyMemberHistorySchema,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.canonical import canonical
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.family_history_status import (
        FamilyHistoryStatus,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for dataAbsentReason
    from spark_auto_mapper_fhir.complex_types.family_history_absent_reason import (
        FamilyHistoryAbsentReason,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for relationship
    from spark_auto_mapper_fhir.complex_types.familial_relationship import (
        FamilialRelationship,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for sex
    from spark_auto_mapper_fhir.complex_types.sex import Sex
    from spark_auto_mapper_fhir.complex_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.complex_types.family_history_reason import (
        FamilyHistoryReason,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.allergy_intolerance import AllergyIntolerance
    from spark_auto_mapper_fhir.resources.questionnaire_response import (
        QuestionnaireResponse,
    )
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation
    from spark_auto_mapper_fhir.backbone_elements.family_member_history_condition import (
        FamilyMemberHistoryCondition,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FamilyMemberHistory(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        instantiatesCanonical: Optional[FhirList[canonical]] = None,
        instantiatesUri: Optional[FhirList[uri]] = None,
        status: FamilyHistoryStatus,
        dataAbsentReason: Optional[CodeableConcept[FamilyHistoryAbsentReason]] = None,
        patient: Reference[Union[Patient]],
        date: Optional[FhirDateTime] = None,
        name: Optional[FhirString] = None,
        relationship: CodeableConcept[FamilialRelationship],
        sex: Optional[CodeableConcept[Sex]] = None,
        estimatedAge: Optional[FhirBoolean] = None,
        reasonCode: Optional[FhirList[CodeableConcept[FamilyHistoryReason]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[
                        Condition,
                        Observation,
                        AllergyIntolerance,
                        QuestionnaireResponse,
                        DiagnosticReport,
                        DocumentReference,
                    ]
                ]
            ]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        condition: Optional[FhirList[FamilyMemberHistoryCondition]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business identifiers assigned to this family member history by the performer
        or other systems which remain constant as the resource is updated and
        propagates from server to server.
            :param instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
        definition that is adhered to in whole or in part by this FamilyMemberHistory.
            :param instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
        other definition that is adhered to in whole or in part by this
        FamilyMemberHistory.
            :param status: A code specifying the status of the record of the family history of a specific
        family member.
            :param dataAbsentReason: Describes why the family member's history is not available.
            :param patient: The person who this history concerns.
            :param date: The date (and possibly time) when the family member history was recorded or
        last updated.
            :param name: This will either be a name or a description; e.g. "Aunt Susan", "my cousin
        with the red hair".
            :param relationship: The type of relationship this person has to the patient (father, mother,
        brother etc.).
            :param sex: The birth sex of the family member.
            :param estimatedAge: If true, indicates that the age value specified is an estimated value.
            :param reasonCode: Describes why the family member history occurred in coded or textual form.
            :param reasonReference: Indicates a Condition, Observation, AllergyIntolerance, or
        QuestionnaireResponse that justifies this family member history event.
            :param note: This property allows a non condition-specific note to the made about the
        related person. Ideally, the note would be in the condition property, but this
        is not always possible.
            :param condition: The significant Conditions (or condition) that the family member had. This is
        a repeating section to allow a system to represent more than one condition per
        resource, though there is nothing stopping multiple resources - one per
        condition.
        """
        super().__init__(
            resourceType="FamilyMemberHistory",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            status=status,
            dataAbsentReason=dataAbsentReason,
            patient=patient,
            date=date,
            name=name,
            relationship=relationship,
            sex=sex,
            estimatedAge=estimatedAge,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            note=note,
            condition=condition,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return FamilyMemberHistorySchema.get_schema(include_extension=include_extension)