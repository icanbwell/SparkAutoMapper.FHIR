from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.searchparameter import SearchParameterSchema

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
    # url (uri)
    # version (string)
    # name (string)
    # derivedFrom (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # status (PublicationStatus)
    from spark_auto_mapper_fhir.value_sets.publication_status import (
        PublicationStatusCode,
    )

    # experimental (boolean)
    # date (dateTime)
    # publisher (string)
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # useContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # jurisdiction (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for jurisdiction
    # purpose (markdown)
    # code (generic_type)
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # base (ResourceType)
    from spark_auto_mapper_fhir.value_sets.resource_type import ResourceTypeCode

    # type_ (SearchParamType)
    from spark_auto_mapper_fhir.value_sets.search_param_type import SearchParamTypeCode

    # expression (string)
    # xpath (string)
    # xpathUsage (XPathUsageType)
    from spark_auto_mapper_fhir.value_sets.x_path_usage_type import XPathUsageTypeCode

    # target (ResourceType)
    # multipleOr (boolean)
    # multipleAnd (boolean)
    # comparator (SearchComparator)
    from spark_auto_mapper_fhir.value_sets.search_comparator import SearchComparatorCode

    # modifier (SearchModifierCode)
    from spark_auto_mapper_fhir.value_sets.search_modifier_code import (
        SearchModifierCodeCode,
    )

    # chain (string)
    # component (SearchParameter.Component)
    from spark_auto_mapper_fhir.backbone_elements.search_parameter_component import (
        SearchParameterComponent,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SearchParameter(FhirResourceBase):
    """
    SearchParameter
    searchparameter.xsd
        A search parameter that defines a named search item that can be used to
    search/filter on a resource.
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
        url: FhirUri,
        version: Optional[FhirString] = None,
        name: FhirString,
        derivedFrom: Optional[FhirCanonical] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: FhirMarkdown,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
        purpose: Optional[FhirMarkdown] = None,
        code: GenericTypeCode,
        base: FhirList[ResourceTypeCode],
        type_: SearchParamTypeCode,
        expression: Optional[FhirString] = None,
        xpath: Optional[FhirString] = None,
        xpathUsage: Optional[XPathUsageTypeCode] = None,
        target: Optional[FhirList[ResourceTypeCode]] = None,
        multipleOr: Optional[FhirBoolean] = None,
        multipleAnd: Optional[FhirBoolean] = None,
        comparator: Optional[FhirList[SearchComparatorCode]] = None,
        modifier: Optional[FhirList[SearchModifierCodeCode]] = None,
        chain: Optional[FhirList[FhirString]] = None,
        component: Optional[FhirList[SearchParameterComponent]] = None,
    ) -> None:
        """
            A search parameter that defines a named search item that can be used to
        search/filter on a resource.
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
            :param url: An absolute URI that is used to identify this search parameter when it is
        referenced in a specification, model, design or an instance; also called its
        canonical identifier. This SHOULD be globally unique and SHOULD be a literal
        address at which at which an authoritative instance of this search parameter
        is (or will be) published. This URL can be the target of a canonical
        reference. It SHALL remain the same when the search parameter is stored on
        different servers.
            :param version: The identifier that is used to identify this version of the search parameter
        when it is referenced in a specification, model, design or instance. This is
        an arbitrary value managed by the search parameter author and is not expected
        to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
        a managed version is not available. There is also no expectation that versions
        can be placed in a lexicographical sequence.
            :param name: A natural language name identifying the search parameter. This name should be
        usable as an identifier for the module by machine processing applications such
        as code generation.
            :param derivedFrom: Where this search parameter is originally defined. If a derivedFrom is
        provided, then the details in the search parameter must be consistent with the
        definition from which it is defined. i.e. the parameter should have the same
        meaning, and (usually) the functionality should be a proper subset of the
        underlying search parameter.
            :param status: The status of this search parameter. Enables tracking the life-cycle of the
        content.
            :param experimental: A Boolean value to indicate that this search parameter is authored for testing
        purposes (or education/evaluation/marketing) and is not intended to be used
        for genuine usage.
            :param date: The date  (and optionally time) when the search parameter was published. The
        date must change when the business version changes and it must change if the
        status code changes. In addition, it should change when the substantive
        content of the search parameter changes.
            :param publisher: The name of the organization or individual that published the search
        parameter.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: And how it used.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate search
        parameter instances.
            :param jurisdiction: A legal or geographic region in which the search parameter is intended to be
        used.
            :param purpose: Explanation of why this search parameter is needed and why it has been
        designed as it has.
            :param code: The code used in the URL or the parameter name in a parameters resource for
        this search parameter.
            :param base: The base resource type(s) that this search parameter can be used against.
            :param type_: The type of value that a search parameter may contain, and how the content is
        interpreted.
            :param expression: A FHIRPath expression that returns a set of elements for the search parameter.
            :param xpath: An XPath expression that returns a set of elements for the search parameter.
            :param xpathUsage: How the search parameter relates to the set of elements returned by evaluating
        the xpath query.
            :param target: Types of resource (if a resource is referenced).
            :param multipleOr: Whether multiple values are allowed for each time the parameter exists. Values
        are separated by commas, and the parameter matches if any of the values match.
            :param multipleAnd: Whether multiple parameters are allowed - e.g. more than one parameter with
        the same name. The search matches if all the parameters match.
            :param comparator: Comparators supported for the search parameter.
            :param modifier: A modifier supported for the search parameter.
            :param chain: Contains the names of any search parameters which may be chained to the
        containing search parameter. Chained parameters may be added to search
        parameters of type reference and specify that resources will only be returned
        if they contain a reference to a resource which matches the chained parameter
        value. Values for this field should be drawn from SearchParameter.code for a
        parameter on the target resource type.
            :param component: Used to define the parts of a composite search parameter.
        """
        super().__init__(
            resourceType="SearchParameter",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            url=url,
            version=version,
            name=name,
            derivedFrom=derivedFrom,
            status=status,
            experimental=experimental,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            code=code,
            base=base,
            type_=type_,
            expression=expression,
            xpath=xpath,
            xpathUsage=xpathUsage,
            target=target,
            multipleOr=multipleOr,
            multipleAnd=multipleAnd,
            comparator=comparator,
            modifier=modifier,
            chain=chain,
            component=component,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return SearchParameterSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
