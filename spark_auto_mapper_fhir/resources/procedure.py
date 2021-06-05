from typing import Optional, Union, TYPE_CHECKING

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.procedure import ProcedureSchema

from spark_auto_mapper_fhir.backbone_elements.procedure_backbone_element import (
    ProcedureBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.procedure_performer_backbone_element import (
    ProcedurePerformerBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.annotation import Annotation
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.range import Range
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.age import FhirAge
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirCanonical, FhirUri
from spark_auto_mapper_fhir.resources.care_plan import CarePlan
from spark_auto_mapper_fhir.resources.composition import Composition

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.condition import Condition
from spark_auto_mapper_fhir.resources.device import Device

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
from spark_auto_mapper_fhir.resources.encounter import Encounter
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.medication import Medication
from spark_auto_mapper_fhir.resources.medication_administration import (
    MedicationAdministration,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.observation import Observation
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.resources.substance import Substance
from spark_auto_mapper_fhir.valuesets.body_site import SNOMEDCTBodyStructuresCode
from spark_auto_mapper_fhir.valuesets.condition import ConditionCode
from spark_auto_mapper_fhir.valuesets.device_kind import DeviceKindCode
from spark_auto_mapper_fhir.valuesets.event_status import EventStatusCode
from spark_auto_mapper_fhir.valuesets.procedure_reason import ProcedureReasonCode
from spark_auto_mapper_fhir.valuesets.snomed import SnoMedCode
from spark_auto_mapper_fhir.valuesets.snomed_procedure import SNOMEDCTProcedureCode


class Procedure(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: EventStatusCode,
        statusReason: Optional[CodeableConcept[SnoMedCode]] = None,
        subject: Reference[Union[Patient, Group]],
        instantiatesCanonical: Optional[FhirCanonical] = None,
        instantiatesUri: Optional[FhirList[FhirUri]],
        basedOn: Optional[FhirList[Union[CarePlan, ServiceRequest]]] = None,
        partOf: Optional[
            FhirList[Union["Procedure", "Observation", MedicationAdministration]]
        ] = None,
        category: Optional[CodeableConcept[SnoMedCode]] = None,
        code: Optional[CodeableConcept[SNOMEDCTProcedureCode]] = None,
        performedDateTime: Optional[FhirDateTime] = None,
        performedPeriod: Optional[Period] = None,
        performedString: Optional[FhirString] = None,
        performedAge: Optional[FhirAge] = None,
        performedRange: Optional[Range] = None,
        encounter: Optional[Encounter] = None,
        recorder: Optional[
            Reference[Union[Patient, RelatedPerson, Practitioner, PractitionerRole]]
        ] = None,
        asserter: Optional[
            Reference[Union[Patient, RelatedPerson, Practitioner, PractitionerRole]]
        ] = None,
        performer: Optional[FhirList[ProcedurePerformerBackboneElement]] = None,
        location: Optional[Reference[Location]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[ProcedureReasonCode]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[
                        "Condition",
                        "Observation",
                        "Procedure",
                        "DiagnosticReport",
                        DocumentReference,
                    ]
                ]
            ]
        ] = None,
        bodySite: Optional[
            FhirList[CodeableConcept[SNOMEDCTBodyStructuresCode]]
        ] = None,
        outcome: Optional[CodeableConcept[SNOMEDCTProcedureCode]] = None,
        report: Optional[
            FhirList[
                Reference[Union["DiagnosticReport", DocumentReference, Composition]]
            ]
        ] = None,
        complication: Optional[FhirList[CodeableConcept[ConditionCode]]] = None,
        complicationDetail: Optional[Reference["Condition"]] = None,
        followUp: Optional[FhirList[CodeableConcept[SNOMEDCTProcedureCode]]] = None,
        note: Optional[Annotation] = None,
        focalDevice: Optional[FhirList[ProcedureBackboneElement]] = None,
        usedReference: Optional[
            FhirList[Reference[Union[Device, Medication, Substance]]]
        ] = None,
        usedCode: Optional[FhirList[CodeableConcept[DeviceKindCode]]] = None,
    ):
        """
        Procedure Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Procedure
        An action that is being or was performed on a patient


        :param id_: id of resource
        :param status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
        :param statusReason: Reason for current status
        :param subject: Who the procedure was performed on
        :param instantiatesCanonical: Instantiates FHIR protocol or definition
        :param instantiatesUri: Instantiates external protocol or definition
        :param basedOn: A request for this procedure
        :param partOf: Part of referenced event
        :param category: Classification of the procedure
        :param code: Identification of the procedure
        :param encounter: Encounter created as part of
        :param recorder: Who recorded the procedure
        :param asserter: Person who asserts this procedure
        :param performer: The people who performed the procedure
        :param location: Where the procedure happened
        :param reasonCode: Coded reason procedure performed
        :param reasonReference: The justification that the procedure was performed
        :param outcome: The result of procedure
        :param report: Any report resulting from the procedure
        :param complication: Complication following the procedure
        :param complicationDetail: A condition that is a result of the procedure
        :param followUp: Instructions for follow up
        :param note: Additional information about the procedure
        :param focalDevice: Manipulated, implanted, or removed device
        :param usedReference: Items used during procedure
        :param usedCode: Coded items used during the procedure

        """

        super().__init__(
            resourceType="Procedure",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,  # Do more investigation on this
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            partOf=partOf,
            status=status,
            statusReason=statusReason,
            category=category,
            code=code,
            subject=subject,
            encounter=encounter,
            performedDateTime=performedDateTime,
            performedPeriod=performedPeriod,
            performedString=performedString,
            performedAge=performedAge,
            performedRange=performedRange,
            recorder=recorder,
            asserter=asserter,
            performer=performer,
            location=location,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            bodySite=bodySite,
            outcome=outcome,
            report=report,
            complication=complication,
            complicationDetail=complicationDetail,
            followUp=followUp,
            note=note,
            focalDevice=focalDevice,
            usedReference=usedReference,
            usedCode=usedCode,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ProcedureSchema.get_schema(include_extension=include_extension)
