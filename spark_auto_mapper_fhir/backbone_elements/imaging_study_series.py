from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # uid (id)
    # number (unsignedInt)
    from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt

    # modality (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for modality
    # Import for CodeableConcept for modality
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for modality
    # description (string)
    # numberOfInstances (unsignedInt)
    # endpoint (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for endpoint
    from spark_auto_mapper_fhir.resources.endpoint import Endpoint

    # bodySite (Coding)
    # End Import for References for bodySite
    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodySite
    # laterality (Coding)
    # End Import for References for laterality
    # Import for CodeableConcept for laterality
    from spark_auto_mapper_fhir.value_sets.laterality import LateralityCode

    # End Import for CodeableConcept for laterality
    # specimen (Reference)
    # Imports for References for specimen
    from spark_auto_mapper_fhir.resources.specimen import Specimen

    # started (dateTime)
    # performer (ImagingStudy.Performer)
    from spark_auto_mapper_fhir.backbone_elements.imaging_study_performer import (
        ImagingStudyPerformer,
    )

    # instance (ImagingStudy.Instance)
    from spark_auto_mapper_fhir.backbone_elements.imaging_study_instance import (
        ImagingStudyInstance,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImagingStudySeries(FhirBackboneElementBase):
    """
    ImagingStudy.Series
        Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        uid: FhirId,
        number: Optional[FhirUnsignedInt] = None,
        modality: Coding[GenericTypeCode],
        description: Optional[FhirString] = None,
        numberOfInstances: Optional[FhirUnsignedInt] = None,
        endpoint: Optional[FhirList[Reference[Endpoint]]] = None,
        bodySite: Optional[Coding[SNOMEDCTBodyStructuresCode]] = None,
        laterality: Optional[Coding[LateralityCode]] = None,
        specimen: Optional[FhirList[Reference[Specimen]]] = None,
        started: Optional[FhirDateTime] = None,
        performer: Optional[FhirList[ImagingStudyPerformer]] = None,
        instance: Optional[FhirList[ImagingStudyInstance]] = None,
    ) -> None:
        """
            Representation of the content produced in a DICOM imaging study. A study
        comprises a set of series, each of which includes a set of Service-Object Pair
        Instances (SOP Instances - images or other data) acquired or produced in a
        common context.  A series is of only one modality (e.g. X-ray, CT, MR,
        ultrasound), but a study may have multiple series of different modalities.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param uid: The DICOM Series Instance UID for the series.
            :param number: The numeric identifier of this series in the study.
            :param modality: The modality of this series sequence.
            :param description: A description of the series.
            :param numberOfInstances: Number of SOP Instances in the Study. The value given may be larger than the
        number of instance elements this resource contains due to resource
        availability, security, or other factors. This element should be present if
        any instance elements are present.
            :param endpoint: The network service providing access (e.g., query, view, or retrieval) for
        this series. See implementation notes for information about using DICOM
        endpoints. A series-level endpoint, if present, has precedence over a study-
        level endpoint with the same Endpoint.connectionType.
            :param bodySite: The anatomic structures examined. See DICOM Part 16 Annex L (http://dicom.nema
        .org/medical/dicom/current/output/chtml/part16/chapter_L.html) for DICOM to
        SNOMED-CT mappings. The bodySite may indicate the laterality of body part
        imaged; if so, it shall be consistent with any content of
        ImagingStudy.series.laterality.
            :param laterality: The laterality of the (possibly paired) anatomic structures examined. E.g.,
        the left knee, both lungs, or unpaired abdomen. If present, shall be
        consistent with any laterality information indicated in
        ImagingStudy.series.bodySite.
            :param specimen: The specimen imaged, e.g., for whole slide imaging of a biopsy.
            :param started: The date and time the series was started.
            :param performer: Indicates who or what performed the series and how they were involved.
            :param instance: A single SOP instance within the series, e.g. an image, or presentation state.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            uid=uid,
            number=number,
            modality=modality,
            description=description,
            numberOfInstances=numberOfInstances,
            endpoint=endpoint,
            bodySite=bodySite,
            laterality=laterality,
            specimen=specimen,
            started=started,
            performer=performer,
            instance=instance,
        )
