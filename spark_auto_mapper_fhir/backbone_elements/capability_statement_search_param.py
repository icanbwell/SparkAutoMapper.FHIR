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
    # name (string)
    # definition (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # type_ (SearchParamType)
    from spark_auto_mapper_fhir.value_sets.search_param_type import SearchParamTypeCode

    # documentation (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatementSearchParam(FhirBackboneElementBase):
    """
    CapabilityStatement.SearchParam
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        name: FhirString,
        definition: Optional[FhirCanonical] = None,
        type_: SearchParamTypeCode,
        documentation: Optional[FhirMarkdown] = None,
    ) -> None:
        """
            A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server for a particular version of FHIR that may be used as a statement of
        actual server functionality or a statement of required or desired server
        implementation.

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
            :param name: The name of the search parameter used in the interface.
            :param definition: An absolute URI that is a formal reference to where this parameter was first
        defined, so that a client can be confident of the meaning of the search
        parameter (a reference to [[[SearchParameter.url]]]). This element SHALL be
        populated if the search parameter refers to a SearchParameter defined by the
        FHIR core specification or externally defined IGs.
            :param type_: The type of value a search parameter refers to, and how the content is
        interpreted.
            :param documentation: This allows documentation of any distinct behaviors about how the search
        parameter is used.  For example, text matching algorithms.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            name=name,
            definition=definition,
            type_=type_,
            documentation=documentation,
        )
