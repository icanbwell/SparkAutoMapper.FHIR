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
from spark_fhir_schemas.r4.resources.searchparameter import SearchParameterSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.canonical import canonical
    from spark_auto_mapper_fhir.complex_types.publication_status import (
        PublicationStatus,
    )
    from spark_auto_mapper_fhir.complex_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail
    from spark_auto_mapper_fhir.complex_types.markdown import markdown
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.complex_types.jurisdiction import Jurisdiction
    from spark_auto_mapper_fhir.complex_types.markdown import markdown
    from spark_auto_mapper_fhir.complex_types.code import code
    from spark_auto_mapper_fhir.complex_types.code import code
    from spark_auto_mapper_fhir.complex_types.search_param_type import SearchParamType
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.x_path_usage_type import XPathUsageType
    from spark_auto_mapper_fhir.complex_types.code import code
    from spark_auto_mapper_fhir.complex_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.complex_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.complex_types.search_comparator import SearchComparator
    from spark_auto_mapper_fhir.complex_types.search_modifier_code import (
        SearchModifierCode,
    )
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.backbone_elements.search_parameter_component import (
        SearchParameterComponent,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SearchParameter(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        url: uri,
        version: Optional[FhirString] = None,
        name: FhirString,
        derivedFrom: Optional[canonical] = None,
        status: PublicationStatus,
        experimental: Optional[FhirBoolean] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: markdown,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[FhirList[CodeableConcept[Jurisdiction]]] = None,
        purpose: Optional[markdown] = None,
        code: code,
        base: FhirList[code],
        type: SearchParamType,
        expression: Optional[FhirString] = None,
        xpath: Optional[FhirString] = None,
        xpathUsage: Optional[XPathUsageType] = None,
        target: Optional[FhirList[code]] = None,
        multipleOr: Optional[FhirBoolean] = None,
        multipleAnd: Optional[FhirBoolean] = None,
        comparator: Optional[FhirList[SearchComparator]] = None,
        modifier: Optional[FhirList[SearchModifierCode]] = None,
        chain: Optional[FhirList[FhirString]] = None,
        component: Optional[FhirList[SearchParameterComponent]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
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
            :param type: The type of value that a search parameter may contain, and how the content is
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
            extension=extension,
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
            type=type,
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

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return SearchParameterSchema.get_schema(include_extension=include_extension)