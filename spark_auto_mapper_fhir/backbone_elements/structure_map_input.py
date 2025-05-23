from __future__ import annotations
from typing import Optional, TYPE_CHECKING

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
    # name (id)
    # type_ (string)
    # mode (StructureMapInputMode)
    from spark_auto_mapper_fhir.value_sets.structure_map_input_mode import (
        StructureMapInputModeCode,
    )

    # documentation (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StructureMapInput(FhirBackboneElementBase):
    """
    StructureMap.Input
        A Map of relationships between 2 structures that can be used to transform data.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        name: FhirId,
        type_: Optional[FhirString] = None,
        mode: StructureMapInputModeCode,
        documentation: Optional[FhirString] = None,
    ) -> None:
        """
            A Map of relationships between 2 structures that can be used to transform
        data.

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
            :param name: Name for this instance of data.
            :param type_: Type for this instance of data.
            :param mode: Mode for this instance of data.
            :param documentation: Documentation for this instance of data.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            name=name,
            type_=type_,
            mode=mode,
            documentation=documentation,
        )
