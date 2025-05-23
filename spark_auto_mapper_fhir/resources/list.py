from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

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
from spark_fhir_schemas.r4.resources.list import ListSchema

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

    # status (ListStatus)
    from spark_auto_mapper_fhir.value_sets.list_status import ListStatusCode

    # mode (ListMode)
    from spark_auto_mapper_fhir.value_sets.list_mode import ListModeCode

    # title (string)
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.example_use_codes_for_list import (
        ExampleUseCodesForListCode,
    )

    # End Import for CodeableConcept for code
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.location import Location

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # date (dateTime)
    # source (Reference)
    # Imports for References for source
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # orderedBy (CodeableConcept)
    # Import for CodeableConcept for orderedBy
    from spark_auto_mapper_fhir.value_sets.list_order_codes import ListOrderCodesCode

    # End Import for CodeableConcept for orderedBy
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # entry (List.Entry)
    from spark_auto_mapper_fhir.backbone_elements.list_entry import ListEntry

    # emptyReason (CodeableConcept)
    # Import for CodeableConcept for emptyReason
    from spark_auto_mapper_fhir.value_sets.list_empty_reasons import (
        ListEmptyReasonsCode,
    )

    # End Import for CodeableConcept for emptyReason


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class List_(FhirResourceBase):
    """
    List
    list.xsd
        A list is a curated collection of resources.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        use_date_for: Optional[List[str]] = None,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: ListStatusCode,
        mode: ListModeCode,
        title: Optional[FhirString] = None,
        code: Optional[CodeableConcept[ExampleUseCodesForListCode]] = None,
        subject: Optional[Reference[Union[Patient, Group, Device, Location]]] = None,
        encounter: Optional[Reference[Encounter]] = None,
        date: Optional[FhirDateTime] = None,
        source: Optional[
            Reference[Union[Practitioner, PractitionerRole, Patient, Device]]
        ] = None,
        orderedBy: Optional[CodeableConcept[ListOrderCodesCode]] = None,
        note: Optional[FhirList[Annotation]] = None,
        entry: Optional[FhirList[ListEntry]] = None,
        emptyReason: Optional[CodeableConcept[ListEmptyReasonsCode]] = None,
    ) -> None:
        """
            A list is a curated collection of resources.
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
            :param identifier: Identifier for the List assigned for business purposes outside the context of
        FHIR.
            :param status: Indicates the current state of this list.
            :param mode: How this list was prepared - whether it is a working list that is suitable for
        being maintained on an ongoing basis, or if it represents a snapshot of a list
        of items from another source, or whether it is a prepared list where items may
        be marked as added, modified or deleted.
            :param title: A label for the list assigned by the author.
            :param code: This code defines the purpose of the list - why it was created.
            :param subject: The common subject (or patient) of the resources that are in the list if there
        is one.
            :param encounter: The encounter that is the context in which this list was created.
            :param date: The date that the list was prepared.
            :param source: The entity responsible for deciding what the contents of the list were. Where
        the list was created by a human, this is the same as the author of the list.
            :param orderedBy: What order applies to the items in the list.
            :param note: Comments that apply to the overall list.
            :param entry: Entries in this list.
            :param emptyReason: If the list is empty, why the list is empty.
        """
        super().__init__(
            resourceType="List",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            status=status,
            mode=mode,
            title=title,
            code=code,
            subject=subject,
            encounter=encounter,
            date=date,
            source=source,
            orderedBy=orderedBy,
            note=note,
            entry=entry,
            emptyReason=emptyReason,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return ListSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
