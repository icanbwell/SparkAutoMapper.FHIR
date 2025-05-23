from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
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
    # subunit (integer)
    # sequence (string)
    # length (integer)
    # sequenceAttachment (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment

    # fivePrime (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for fivePrime
    # Import for CodeableConcept for fivePrime
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for fivePrime
    # threePrime (CodeableConcept)
    # End Import for References for threePrime
    # Import for CodeableConcept for threePrime
    # End Import for CodeableConcept for threePrime
    # linkage (SubstanceNucleicAcid.Linkage)
    from spark_auto_mapper_fhir.backbone_elements.substance_nucleic_acid_linkage import (
        SubstanceNucleicAcidLinkage,
    )

    # sugar (SubstanceNucleicAcid.Sugar)
    from spark_auto_mapper_fhir.backbone_elements.substance_nucleic_acid_sugar import (
        SubstanceNucleicAcidSugar,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceNucleicAcidSubunit(FhirBackboneElementBase):
    """
    SubstanceNucleicAcid.Subunit
        Nucleic acids are defined by three distinct elements: the base, sugar and linkage. Individual substance/moiety IDs will be created for each of these elements. The nucleotide sequence will be always entered in the 5’-3’ direction.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        subunit: Optional[FhirInteger] = None,
        sequence: Optional[FhirString] = None,
        length: Optional[FhirInteger] = None,
        sequenceAttachment: Optional[Attachment] = None,
        fivePrime: Optional[CodeableConcept[GenericTypeCode]] = None,
        threePrime: Optional[CodeableConcept[GenericTypeCode]] = None,
        linkage: Optional[FhirList[SubstanceNucleicAcidLinkage]] = None,
        sugar: Optional[FhirList[SubstanceNucleicAcidSugar]] = None,
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
            :param subunit: Index of linear sequences of nucleic acids in order of decreasing length.
        Sequences of the same length will be ordered by molecular weight. Subunits
        that have identical sequences will be repeated and have sequential subscripts.
            :param sequence: Actual nucleotide sequence notation from 5' to 3' end using standard single
        letter codes. In addition to the base sequence, sugar and type of phosphate or
        non-phosphate linkage should also be captured.
            :param length: The length of the sequence shall be captured.
            :param sequenceAttachment: (TBC).
            :param fivePrime: The nucleotide present at the 5’ terminal shall be specified based on a
        controlled vocabulary. Since the sequence is represented from the 5' to the 3'
        end, the 5’ prime nucleotide is the letter at the first position in the
        sequence. A separate representation would be redundant.
            :param threePrime: The nucleotide present at the 3’ terminal shall be specified based on a
        controlled vocabulary. Since the sequence is represented from the 5' to the 3'
        end, the 5’ prime nucleotide is the letter at the last position in the
        sequence. A separate representation would be redundant.
            :param linkage: The linkages between sugar residues will also be captured.
            :param sugar: 5.3.6.8.1 Sugar ID (Mandatory).
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            subunit=subunit,
            sequence=sequence,
            length=length,
            sequenceAttachment=sequenceAttachment,
            fivePrime=fivePrime,
            threePrime=threePrime,
            linkage=linkage,
            sugar=sugar,
        )
