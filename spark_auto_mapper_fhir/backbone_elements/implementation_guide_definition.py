from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # grouping (ImplementationGuide.Grouping)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_grouping import (
        ImplementationGuideGrouping,
    )

    # resource (ImplementationGuide.Resource)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_resource import (
        ImplementationGuideResource,
    )

    # page (ImplementationGuide.Page)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_page import (
        ImplementationGuidePage,
    )

    # parameter (ImplementationGuide.Parameter)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_parameter import (
        ImplementationGuideParameter,
    )

    # template (ImplementationGuide.Template)
    from spark_auto_mapper_fhir.backbone_elements.implementation_guide_template import (
        ImplementationGuideTemplate,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImplementationGuideDefinition(FhirBackboneElementBase):
    """
    ImplementationGuide.Definition
        A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        grouping: Optional[FhirList[ImplementationGuideGrouping]] = None,
        resource: FhirList[ImplementationGuideResource],
        page: Optional[ImplementationGuidePage] = None,
        parameter: Optional[FhirList[ImplementationGuideParameter]] = None,
        template: Optional[FhirList[ImplementationGuideTemplate]] = None,
    ) -> None:
        """
            A set of rules of how a particular interoperability or standards problem is
        solved - typically through the use of FHIR resources. This resource is used to
        gather all the parts of an implementation guide into a logical whole and to
        publish a computable definition of all the parts.

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
            :param grouping: A logical group of resources. Logical groups can be used when building pages.
            :param resource: A resource that is part of the implementation guide. Conformance resources
        (value set, structure definition, capability statements etc.) are obvious
        candidates for inclusion, but any kind of resource can be included as an
        example resource.
            :param page: A page / section in the implementation guide. The root page is the
        implementation guide home page.
            :param parameter: Defines how IG is built by tools.
            :param template: A template for building resources.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            grouping=grouping,
            resource=resource,
            page=page,
            parameter=parameter,
            template=template,
        )
