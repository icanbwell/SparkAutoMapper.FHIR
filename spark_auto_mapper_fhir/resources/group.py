from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.group import GroupSchema

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

    # active (boolean)
    # type_ (GroupType)
    from spark_auto_mapper_fhir.value_sets.group_type import GroupTypeCode

    # actual (boolean)
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code
    # name (string)
    # quantity (unsignedInt)
    from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt

    # managingEntity (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for managingEntity
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # characteristic (Group.Characteristic)
    from spark_auto_mapper_fhir.backbone_elements.group_characteristic import (
        GroupCharacteristic,
    )

    # member (Group.Member)
    from spark_auto_mapper_fhir.backbone_elements.group_member import GroupMember


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Group(FhirResourceBase):
    """
    Group
    group.xsd
        Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively, and are not
    formally or legally recognized; i.e. a collection of entities that isn't an
    Organization.
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
        active: Optional[FhirBoolean] = None,
        type_: GroupTypeCode,
        actual: FhirBoolean,
        code: Optional[CodeableConcept[GenericTypeCode]] = None,
        name: Optional[FhirString] = None,
        quantity: Optional[FhirUnsignedInt] = None,
        managingEntity: Optional[
            Reference[
                Union[Organization, RelatedPerson, Practitioner, PractitionerRole]
            ]
        ] = None,
        characteristic: Optional[FhirList[GroupCharacteristic]] = None,
        member: Optional[FhirList[GroupMember]] = None,
    ) -> None:
        """
            Represents a defined collection of entities that may be discussed or acted
        upon collectively but which are not expected to act collectively, and are not
        formally or legally recognized; i.e. a collection of entities that isn't an
        Organization.
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
            :param identifier: A unique business identifier for this group.
            :param active: Indicates whether the record for the group is available for use or is merely
        being retained for historical purposes.
            :param type_: Identifies the broad classification of the kind of resources the group
        includes.
            :param actual: If true, indicates that the resource refers to a specific group of real
        individuals.  If false, the group defines a set of intended individuals.
            :param code: Provides a specific type of resource the group includes; e.g. "cow",
        "syringe", etc.
            :param name: A label assigned to the group for human identification and communication.
            :param quantity: A count of the number of resource instances that are part of the group.
            :param managingEntity: Entity responsible for defining and maintaining Group characteristics and/or
        registered members.
            :param characteristic: Identifies traits whose presence r absence is shared by members of the group.
            :param member: Identifies the resource instances that are members of the group.
        """
        super().__init__(
            resourceType="Group",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            active=active,
            type_=type_,
            actual=actual,
            code=code,
            name=name,
            quantity=quantity,
            managingEntity=managingEntity,
            characteristic=characteristic,
            member=member,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return GroupSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
