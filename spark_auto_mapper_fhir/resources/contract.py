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
from spark_fhir_schemas.r4.resources.contract import ContractSchema

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

    # url (uri)
    # version (string)
    # status (ContractResourceStatusCodes)
    from spark_auto_mapper_fhir.value_sets.contract_resource_status_codes import (
        ContractResourceStatusCodesCode,
    )

    # legalState (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for legalState
    from spark_auto_mapper_fhir.value_sets.contract_resource_legal_state_codes import (
        ContractResourceLegalStateCodesCode,
    )

    # End Import for CodeableConcept for legalState
    # instantiatesCanonical (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for instantiatesCanonical
    # instantiatesUri (uri)
    # contentDerivative (CodeableConcept)
    # Import for CodeableConcept for contentDerivative
    from spark_auto_mapper_fhir.value_sets.contract_content_derivation_codes import (
        ContractContentDerivationCodesCode,
    )

    # End Import for CodeableConcept for contentDerivative
    # issued (dateTime)
    # applies (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # expirationType (CodeableConcept)
    # Import for CodeableConcept for expirationType
    from spark_auto_mapper_fhir.value_sets.contract_resource_expiration_type_codes import (
        ContractResourceExpirationTypeCodesCode,
    )

    # End Import for CodeableConcept for expirationType
    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.resource import Resource

    # authority (Reference)
    # Imports for References for authority
    from spark_auto_mapper_fhir.resources.organization import Organization

    # domain (Reference)
    # Imports for References for domain
    from spark_auto_mapper_fhir.resources.location import Location

    # site (Reference)
    # Imports for References for site
    # name (string)
    # title (string)
    # subtitle (string)
    # alias (string)
    # author (Reference)
    # Imports for References for author
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # scope (CodeableConcept)
    # Import for CodeableConcept for scope
    from spark_auto_mapper_fhir.value_sets.contract_resource_scope_codes import (
        ContractResourceScopeCodesCode,
    )

    # End Import for CodeableConcept for scope
    # topicCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for topicCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for topicCodeableConcept
    # topicReference (Reference)
    # Imports for References for topicReference
    # type_ (CodeableConcept)
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.contract_type_codes import (
        ContractTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # subType (CodeableConcept)
    # Import for CodeableConcept for subType
    from spark_auto_mapper_fhir.value_sets.contract_subtype_codes import (
        ContractSubtypeCodesCode,
    )

    # End Import for CodeableConcept for subType
    # contentDefinition (Contract.ContentDefinition)
    from spark_auto_mapper_fhir.backbone_elements.contract_content_definition import (
        ContractContentDefinition,
    )

    # term (Contract.Term)
    from spark_auto_mapper_fhir.backbone_elements.contract_term import ContractTerm

    # supportingInfo (Reference)
    # Imports for References for supportingInfo
    # relevantHistory (Reference)
    # Imports for References for relevantHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance

    # signer (Contract.Signer)
    from spark_auto_mapper_fhir.backbone_elements.contract_signer import ContractSigner

    # friendly (Contract.Friendly)
    from spark_auto_mapper_fhir.backbone_elements.contract_friendly import (
        ContractFriendly,
    )

    # legal (Contract.Legal)
    from spark_auto_mapper_fhir.backbone_elements.contract_legal import ContractLegal

    # rule (Contract.Rule)
    from spark_auto_mapper_fhir.backbone_elements.contract_rule import ContractRule

    # legallyBindingAttachment (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment

    # legallyBindingReference (Reference)
    # Imports for References for legallyBindingReference
    from spark_auto_mapper_fhir.resources.composition import Composition
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.resources.questionnaire_response import (
        QuestionnaireResponse,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Contract(FhirResourceBase):
    """
    Contract
    contract.xsd
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
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
        url: Optional[FhirUri] = None,
        version: Optional[FhirString] = None,
        status: Optional[ContractResourceStatusCodesCode] = None,
        legalState: Optional[
            CodeableConcept[ContractResourceLegalStateCodesCode]
        ] = None,
        instantiatesCanonical: Optional[Reference[Contract]] = None,
        instantiatesUri: Optional[FhirUri] = None,
        contentDerivative: Optional[
            CodeableConcept[ContractContentDerivationCodesCode]
        ] = None,
        issued: Optional[FhirDateTime] = None,
        applies: Optional[Period] = None,
        expirationType: Optional[
            CodeableConcept[ContractResourceExpirationTypeCodesCode]
        ] = None,
        subject: Optional[FhirList[Reference[Resource]]] = None,
        authority: Optional[FhirList[Reference[Organization]]] = None,
        domain: Optional[FhirList[Reference[Location]]] = None,
        site: Optional[FhirList[Reference[Location]]] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        alias: Optional[FhirList[FhirString]] = None,
        author: Optional[
            Reference[Union[Patient, Practitioner, PractitionerRole, Organization]]
        ] = None,
        scope: Optional[CodeableConcept[ContractResourceScopeCodesCode]] = None,
        topicCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        topicReference: Optional[Reference[Resource]] = None,
        type_: Optional[CodeableConcept[ContractTypeCodesCode]] = None,
        subType: Optional[FhirList[CodeableConcept[ContractSubtypeCodesCode]]] = None,
        contentDefinition: Optional[ContractContentDefinition] = None,
        term: Optional[FhirList[ContractTerm]] = None,
        supportingInfo: Optional[FhirList[Reference[Resource]]] = None,
        relevantHistory: Optional[FhirList[Reference[Provenance]]] = None,
        signer: Optional[FhirList[ContractSigner]] = None,
        friendly: Optional[FhirList[ContractFriendly]] = None,
        legal: Optional[FhirList[ContractLegal]] = None,
        rule: Optional[FhirList[ContractRule]] = None,
        legallyBindingAttachment: Optional[Attachment] = None,
        legallyBindingReference: Optional[
            Reference[
                Union[Composition, DocumentReference, QuestionnaireResponse, Contract]
            ]
        ] = None,
    ) -> None:
        """
            Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.
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
            :param identifier: Unique identifier for this Contract or a derivative that references a Source
        Contract.
            :param url: Canonical identifier for this contract, represented as a URI (globally
        unique).
            :param version: An edition identifier used for business purposes to label business significant
        variants.
            :param status: The status of the resource instance.
            :param legalState: Legal states of the formation of a legal instrument, which is a formally
        executed written document that can be formally attributed to its author,
        records and formally expresses a legally enforceable act, process, or
        contractual duty, obligation, or right, and therefore evidences that act,
        process, or agreement.
            :param instantiatesCanonical: The URL pointing to a FHIR-defined Contract Definition that is adhered to in
        whole or part by this Contract.
            :param instantiatesUri: The URL pointing to an externally maintained definition that is adhered to in
        whole or in part by this Contract.
            :param contentDerivative: The minimal content derived from the basal information source at a specific
        stage in its lifecycle.
            :param issued: When this  Contract was issued.
            :param applies: Relevant time or time-period when this Contract is applicable.
            :param expirationType: Event resulting in discontinuation or termination of this Contract instance by
        one or more parties to the contract.
            :param subject: The target entity impacted by or of interest to parties to the agreement.
            :param authority: A formally or informally recognized grouping of people, principals,
        organizations, or jurisdictions formed for the purpose of achieving some form
        of collective action such as the promulgation, administration and enforcement
        of contracts and policies.
            :param domain: Recognized governance framework or system operating with a circumscribed scope
        in accordance with specified principles, policies, processes or procedures for
        managing rights, actions, or behaviors of parties or principals relative to
        resources.
            :param site: Sites in which the contract is complied with,  exercised, or in force.
            :param name: A natural language name identifying this Contract definition, derivative, or
        instance in any legal state. Provides additional information about its
        content. This name should be usable as an identifier for the module by machine
        processing applications such as code generation.
            :param title: A short, descriptive, user-friendly title for this Contract definition,
        derivative, or instance in any legal state.t giving additional information
        about its content.
            :param subtitle: An explanatory or alternate user-friendly title for this Contract definition,
        derivative, or instance in any legal state.t giving additional information
        about its content.
            :param alias: Alternative representation of the title for this Contract definition,
        derivative, or instance in any legal state., e.g., a domain specific contract
        number related to legislation.
            :param author: The individual or organization that authored the Contract definition,
        derivative, or instance in any legal state.
            :param scope: A selector of legal concerns for this Contract definition, derivative, or
        instance in any legal state.
            :param topicCodeableConcept: None
            :param topicReference: None
            :param type_: A high-level category for the legal instrument, whether constructed as a
        Contract definition, derivative, or instance in any legal state.  Provides
        additional information about its content within the context of the Contract's
        scope to distinguish the kinds of systems that would be interested in the
        contract.
            :param subType: Sub-category for the Contract that distinguishes the kinds of systems that
        would be interested in the Contract within the context of the Contract's
        scope.
            :param contentDefinition: Precusory content developed with a focus and intent of supporting the
        formation a Contract instance, which may be associated with and transformable
        into a Contract.
            :param term: One or more Contract Provisions, which may be related and conveyed as a group,
        and may contain nested groups.
            :param supportingInfo: Information that may be needed by/relevant to the performer in their execution
        of this term action.
            :param relevantHistory: Links to Provenance records for past versions of this Contract definition,
        derivative, or instance, which identify key state transitions or updates that
        are likely to be relevant to a user looking at the current version of the
        Contract.  The Provence.entity indicates the target that was changed in the
        update. http://build.fhir.org/provenance-definitions.html#Provenance.entity.
            :param signer: Parties with legal standing in the Contract, including the principal parties,
        the grantor(s) and grantee(s), which are any person or organization bound by
        the contract, and any ancillary parties, which facilitate the execution of the
        contract such as a notary or witness.
            :param friendly: The "patient friendly language" versionof the Contract in whole or in parts.
        "Patient friendly language" means the representation of the Contract and
        Contract Provisions in a manner that is readily accessible and understandable
        by a layperson in accordance with best practices for communication styles that
        ensure that those agreeing to or signing the Contract understand the roles,
        actions, obligations, responsibilities, and implication of the agreement.
            :param legal: List of Legal expressions or representations of this Contract.
            :param rule: List of Computable Policy Rule Language Representations of this Contract.
            :param legallyBindingAttachment: None
            :param legallyBindingReference: None
        """
        super().__init__(
            resourceType="Contract",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            url=url,
            version=version,
            status=status,
            legalState=legalState,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            contentDerivative=contentDerivative,
            issued=issued,
            applies=applies,
            expirationType=expirationType,
            subject=subject,
            authority=authority,
            domain=domain,
            site=site,
            name=name,
            title=title,
            subtitle=subtitle,
            alias=alias,
            author=author,
            scope=scope,
            topicCodeableConcept=topicCodeableConcept,
            topicReference=topicReference,
            type_=type_,
            subType=subType,
            contentDefinition=contentDefinition,
            term=term,
            supportingInfo=supportingInfo,
            relevantHistory=relevantHistory,
            signer=signer,
            friendly=friendly,
            legal=legal,
            rule=rule,
            legallyBindingAttachment=legallyBindingAttachment,
            legallyBindingReference=legallyBindingReference,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ContractSchema.get_schema(include_extension=include_extension)
