from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.provenance import ProvenanceSchema

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
    # target (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for target
    from spark_auto_mapper_fhir.resources.resource import Resource

    # occurredPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # occurredDateTime (dateTime)
    # recorded (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # policy (uri)
    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # reason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for reason
    from spark_auto_mapper_fhir.value_sets.purpose_of_use import PurposeOfUse

    # End Import for CodeableConcept for reason
    # activity (CodeableConcept)
    # Import for CodeableConcept for activity
    from spark_auto_mapper_fhir.value_sets.provenance_activity_type import (
        ProvenanceActivityTypeCode,
    )

    # End Import for CodeableConcept for activity
    # agent (Provenance.Agent)
    from spark_auto_mapper_fhir.backbone_elements.provenance_agent import (
        ProvenanceAgent,
    )

    # entity (Provenance.Entity)
    from spark_auto_mapper_fhir.backbone_elements.provenance_entity import (
        ProvenanceEntity,
    )

    # signature (Signature)
    from spark_auto_mapper_fhir.complex_types.signature import Signature


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Provenance(FhirResourceBase):
    """
    Provenance
    provenance.xsd
        Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that resource.
    Provenance provides a critical foundation for assessing authenticity, enabling
    trust, and allowing reproducibility. Provenance assertions are a form of
    contextual metadata and can themselves become important records with their own
    provenance. Provenance statement indicates clinical significance in terms of
    confidence in authenticity, reliability, and trustworthiness, integrity, and
    stage in lifecycle (e.g. Document Completion - has the artifact been legally
    authenticated), all of which may impact security, privacy, and trust policies.
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
        target: FhirList[Reference[Resource]],
        occurredPeriod: Optional[Period] = None,
        occurredDateTime: Optional[FhirDateTime] = None,
        recorded: FhirInstant,
        policy: Optional[FhirList[FhirUri]] = None,
        location: Optional[Reference[Location]] = None,
        reason: Optional[FhirList[CodeableConcept[PurposeOfUse]]] = None,
        activity: Optional[CodeableConcept[ProvenanceActivityTypeCode]] = None,
        agent: FhirList[ProvenanceAgent],
        entity: Optional[FhirList[ProvenanceEntity]] = None,
        signature: Optional[FhirList[Signature]] = None,
    ) -> None:
        """
            Provenance of a resource is a record that describes entities and processes
        involved in producing and delivering or otherwise influencing that resource.
        Provenance provides a critical foundation for assessing authenticity, enabling
        trust, and allowing reproducibility. Provenance assertions are a form of
        contextual metadata and can themselves become important records with their own
        provenance. Provenance statement indicates clinical significance in terms of
        confidence in authenticity, reliability, and trustworthiness, integrity, and
        stage in lifecycle (e.g. Document Completion - has the artifact been legally
        authenticated), all of which may impact security, privacy, and trust policies.
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
            :param target: The Reference(s) that were generated or updated by  the activity described in
        this resource. A provenance can point to more than one target if multiple
        resources were created/updated by the same activity.
            :param occurredPeriod: None
            :param occurredDateTime: None
            :param recorded: The instant of time at which the activity was recorded.
            :param policy: Policy or plan the activity was defined by. Typically, a single activity may
        have multiple applicable policy documents, such as patient consent, guarantor
        funding, etc.
            :param location: Where the activity occurred, if relevant.
            :param reason: The reason that the activity was taking place.
            :param activity: An activity is something that occurs over a period of time and acts upon or
        with entities; it may include consuming, processing, transforming, modifying,
        relocating, using, or generating entities.
            :param agent: An actor taking a role in an activity  for which it can be assigned some
        degree of responsibility for the activity taking place.
            :param entity: An entity used in this activity.
            :param signature: A digital signature on the target Reference(s). The signer should match a
        Provenance.agent. The purpose of the signature is indicated.
        """
        super().__init__(
            resourceType="Provenance",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            target=target,
            occurredPeriod=occurredPeriod,
            occurredDateTime=occurredDateTime,
            recorded=recorded,
            policy=policy,
            location=location,
            reason=reason,
            activity=activity,
            agent=agent,
            entity=entity,
            signature=signature,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return ProvenanceSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
