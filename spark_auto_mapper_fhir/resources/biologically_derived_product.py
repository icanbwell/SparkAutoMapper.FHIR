from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.biologicallyderivedproduct import (
    BiologicallyDerivedProductSchema,
)

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

    # productCategory (BiologicallyDerivedProductCategory)
    from spark_auto_mapper_fhir.value_sets.biologically_derived_product_category import (
        BiologicallyDerivedProductCategoryCode,
    )

    # productCode (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for productCode
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for productCode
    # status (BiologicallyDerivedProductStatus)
    from spark_auto_mapper_fhir.value_sets.biologically_derived_product_status import (
        BiologicallyDerivedProductStatusCode,
    )

    # request (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for request
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # quantity (integer)
    # parent (Reference)
    # Imports for References for parent
    # collection (BiologicallyDerivedProduct.Collection)
    from spark_auto_mapper_fhir.backbone_elements.biologically_derived_product_collection import (
        BiologicallyDerivedProductCollection,
    )

    # processing (BiologicallyDerivedProduct.Processing)
    from spark_auto_mapper_fhir.backbone_elements.biologically_derived_product_processing import (
        BiologicallyDerivedProductProcessing,
    )

    # manipulation (BiologicallyDerivedProduct.Manipulation)
    from spark_auto_mapper_fhir.backbone_elements.biologically_derived_product_manipulation import (
        BiologicallyDerivedProductManipulation,
    )

    # storage (BiologicallyDerivedProduct.Storage)
    from spark_auto_mapper_fhir.backbone_elements.biologically_derived_product_storage import (
        BiologicallyDerivedProductStorage,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class BiologicallyDerivedProduct(FhirResourceBase):
    """
    BiologicallyDerivedProduct
    biologicallyderivedproduct.xsd
        A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
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
        productCategory: Optional[BiologicallyDerivedProductCategoryCode] = None,
        productCode: Optional[CodeableConcept[GenericTypeCode]] = None,
        status: Optional[BiologicallyDerivedProductStatusCode] = None,
        request: Optional[FhirList[Reference[ServiceRequest]]] = None,
        quantity: Optional[FhirInteger] = None,
        parent: Optional[FhirList[Reference[BiologicallyDerivedProduct]]] = None,
        collection: Optional[BiologicallyDerivedProductCollection] = None,
        processing: Optional[FhirList[BiologicallyDerivedProductProcessing]] = None,
        manipulation: Optional[BiologicallyDerivedProductManipulation] = None,
        storage: Optional[FhirList[BiologicallyDerivedProductStorage]] = None,
    ) -> None:
        """
            A material substance originating from a biological entity intended to be
        transplanted or infused
        into another (possibly the same) biological entity.
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
            :param identifier: This records identifiers associated with this biologically derived product
        instance that are defined by business processes and/or used to refer to it
        when a direct URL reference to the resource itself is not appropriate (e.g. in
        CDA documents, or in written / printed documentation).
            :param productCategory: Broad category of this product.
            :param productCode: A code that identifies the kind of this biologically derived product (SNOMED
        Ctcode).
            :param status: Whether the product is currently available.
            :param request: Procedure request to obtain this biologically derived product.
            :param quantity: Number of discrete units within this product.
            :param parent: Parent product (if any).
            :param collection: How this product was collected.
            :param processing: Any processing of the product during collection that does not change the
        fundamental nature of the product. For example adding anti-coagulants during
        the collection of Peripheral Blood Stem Cells.
            :param manipulation: Any manipulation of product post-collection that is intended to alter the
        product.  For example a buffy-coat enrichment or CD8 reduction of Peripheral
        Blood Stem Cells to make it more suitable for infusion.
            :param storage: Product storage.
        """
        super().__init__(
            resourceType="BiologicallyDerivedProduct",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            productCategory=productCategory,
            productCode=productCode,
            status=status,
            request=request,
            quantity=quantity,
            parent=parent,
            collection=collection,
            processing=processing,
            manipulation=manipulation,
            storage=storage,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return BiologicallyDerivedProductSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
