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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # name (string)
    # residueSite (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceNucleicAcidSugar(FhirBackboneElementBase):
    """
    SubstanceNucleicAcid.Sugar
        Nucleic acids are defined by three distinct elements: the base, sugar and linkage. Individual substance/moiety IDs will be created for each of these elements. The nucleotide sequence will be always entered in the 5’-3’ direction.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        name: Optional[FhirString] = None,
        residueSite: Optional[FhirString] = None,
    ) -> None:
        """
            Nucleic acids are defined by three distinct elements: the base, sugar and
        linkage. Individual substance/moiety IDs will be created for each of these
        elements. The nucleotide sequence will be always entered in the 5’-3’
        direction.

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
            :param identifier: The Substance ID of the sugar or sugar-like component that make up the
        nucleotide.
            :param name: The name of the sugar or sugar-like component that make up the nucleotide.
            :param residueSite: The residues that contain a given sugar will be captured. The order of given
        residues will be captured in the 5‘-3‘direction consistent with the base
        sequences listed above.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            name=name,
            residueSite=residueSite,
        )
