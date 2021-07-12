from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.media import MediaSchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # basedOn (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
    from spark_auto_mapper_fhir.resources.care_plan import CarePlan

    # partOf (Reference)
    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.resource import Resource

    # status (EventStatus)
    from spark_auto_mapper_fhir.value_sets.event_status import EventStatusCode

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.media_type import MediaTypeCode

    # End Import for CodeableConcept for type_
    # modality (CodeableConcept)
    # Import for CodeableConcept for modality
    from spark_auto_mapper_fhir.value_sets.media_modality import MediaModalityCode

    # End Import for CodeableConcept for modality
    # view (CodeableConcept)
    # Import for CodeableConcept for view
    from spark_auto_mapper_fhir.value_sets.media_collection_view_or__projection import (
        MediaCollectionView_or_ProjectionCode,
    )

    # End Import for CodeableConcept for view
    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.specimen import Specimen
    from spark_auto_mapper_fhir.resources.location import Location

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # createdDateTime (dateTime)
    # createdPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # issued (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # operator (Reference)
    # Imports for References for operator
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.procedure_reason_codes import (
        ProcedureReasonCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # bodySite (CodeableConcept)
    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodySite
    # deviceName (string)
    # device (Reference)
    # Imports for References for device
    from spark_auto_mapper_fhir.resources.device_metric import DeviceMetric

    # height (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # width (positiveInt)
    # frames (positiveInt)
    # duration (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # content (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Media(FhirResourceBase):
    """
    Media
    media.xsd
        A photo, video, or audio recording acquired or used in healthcare. The actual
    content may be inline or provided by direct reference.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[FhirList[Reference[Union[ServiceRequest, CarePlan]]]] = None,
        partOf: Optional[FhirList[Reference[Resource]]] = None,
        status: EventStatusCode,
        type_: Optional[CodeableConcept[MediaTypeCode]] = None,
        modality: Optional[CodeableConcept[MediaModalityCode]] = None,
        view: Optional[CodeableConcept[MediaCollectionView_or_ProjectionCode]] = None,
        subject: Optional[
            Reference[
                Union[
                    Patient,
                    Practitioner,
                    PractitionerRole,
                    Group,
                    Device,
                    Specimen,
                    Location,
                ]
            ]
        ] = None,
        encounter: Optional[Reference[Encounter]] = None,
        createdDateTime: Optional[FhirDateTime] = None,
        createdPeriod: Optional[Period] = None,
        issued: Optional[FhirInstant] = None,
        operator: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Organization,
                    CareTeam,
                    Patient,
                    Device,
                    RelatedPerson,
                ]
            ]
        ] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[ProcedureReasonCodesCode]]
        ] = None,
        bodySite: Optional[CodeableConcept[SNOMEDCTBodyStructuresCode]] = None,
        deviceName: Optional[FhirString] = None,
        device: Optional[Reference[Union[Device, DeviceMetric, Device]]] = None,
        height: Optional[FhirPositiveInt] = None,
        width: Optional[FhirPositiveInt] = None,
        frames: Optional[FhirPositiveInt] = None,
        duration: Optional[FhirDecimal] = None,
        content: Attachment,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """
            A photo, video, or audio recording acquired or used in healthcare. The actual
        content may be inline or provided by direct reference.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param identifier: Identifiers associated with the image - these may include identifiers for the
        image itself, identifiers for the context of its collection (e.g. series ids)
        and context ids such as accession numbers or other workflow identifiers.
            :param basedOn: A procedure that is fulfilled in whole or in part by the creation of this
        media.
            :param partOf: A larger event of which this particular event is a component or step.
            :param status: The current state of the {{title}}.
            :param type_: A code that classifies whether the media is an image, video or audio recording
        or some other media category.
            :param modality: Details of the type of the media - usually, how it was acquired (what type of
        device). If images sourced from a DICOM system, are wrapped in a Media
        resource, then this is the modality.
            :param view: The name of the imaging view e.g. Lateral or Antero-posterior (AP).
            :param subject: Who/What this Media is a record of.
            :param encounter: The encounter that establishes the context for this media.
            :param createdDateTime: None
            :param createdPeriod: None
            :param issued: The date and time this version of the media was made available to providers,
        typically after having been reviewed.
            :param operator: The person who administered the collection of the image.
            :param reasonCode: Describes why the event occurred in coded or textual form.
            :param bodySite: Indicates the site on the subject's body where the observation was made (i.e.
        the target site).
            :param deviceName: The name of the device / manufacturer of the device  that was used to make the
        recording.
            :param device: The device used to collect the media.
            :param height: Height of the image in pixels (photo/video).
            :param width: Width of the image in pixels (photo/video).
            :param frames: The number of frames in a photo. This is used with a multi-page fax, or an
        imaging acquisition context that takes multiple slices in a single image, or
        an animated gif. If there is more than one frame, this SHALL have a value in
        order to alert interface software that a multi-frame capable rendering widget
        is required.
            :param duration: The duration of the recording in seconds - for audio and video.
            :param content: The actual content of the media - inline or by direct reference to the media
        source file.
            :param note: Comments made about the media by the performer, subject or other participants.
        """
        super().__init__(
            resourceType="Media",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            basedOn=basedOn,
            partOf=partOf,
            status=status,
            type_=type_,
            modality=modality,
            view=view,
            subject=subject,
            encounter=encounter,
            createdDateTime=createdDateTime,
            createdPeriod=createdPeriod,
            issued=issued,
            operator=operator,
            reasonCode=reasonCode,
            bodySite=bodySite,
            deviceName=deviceName,
            device=device,
            height=height,
            width=width,
            frames=frames,
            duration=duration,
            content=content,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MediaSchema.get_schema(include_extension=include_extension)
