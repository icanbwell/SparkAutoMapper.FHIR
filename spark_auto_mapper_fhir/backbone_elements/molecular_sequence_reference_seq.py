from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.orientation_type import orientationType
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for referenceSeqPointer
    from spark_auto_mapper_fhir.resources.molecular_sequence import MolecularSequence
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.strand_type import strandType
    from spark_auto_mapper_fhir.complex_types.integer import integer
    from spark_auto_mapper_fhir.complex_types.integer import integer


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MolecularSequenceReferenceSeq(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        chromosome: Optional[CodeableConcept] = None,
        genomeBuild: Optional[string] = None,
        orientation: Optional[orientationType] = None,
        referenceSeqId: Optional[CodeableConcept] = None,
        referenceSeqPointer: Optional[Reference[Union[MolecularSequence]]] = None,
        referenceSeqString: Optional[string] = None,
        strand: Optional[strandType] = None,
        windowStart: Optional[integer] = None,
        windowEnd: Optional[integer] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param chromosome: Structural unit composed of a nucleic acid molecule which controls its own
        replication through the interaction of specific proteins at one or more
        origins of replication ([SO:0000340](http://www.sequenceontology.org/browser/c
        urrent_svn/term/SO:0000340)).
            :param genomeBuild: The Genome Build used for reference, following GRCh build versions e.g. 'GRCh
        37'.  Version number must be included if a versioned release of a primary
        build was used.
            :param orientation: A relative reference to a DNA strand based on gene orientation. The strand
        that contains the open reading frame of the gene is the "sense" strand, and
        the opposite complementary strand is the "antisense" strand.
            :param referenceSeqId: Reference identifier of reference sequence submitted to NCBI. It must match
        the type in the MolecularSequence.type field. For example, the prefix, “NG_”
        identifies reference sequence for genes, “NM_” for messenger RNA transcripts,
        and “NP_” for amino acid sequences.
            :param referenceSeqPointer: A pointer to another MolecularSequence entity as reference sequence.
            :param referenceSeqString: A string like "ACGT".
            :param strand: An absolute reference to a strand. The Watson strand is the strand whose
        5'-end is on the short arm of the chromosome, and the Crick strand as the one
        whose 5'-end is on the long arm.
            :param windowStart: Start position of the window on the reference sequence. If the coordinate
        system is either 0-based or 1-based, then start position is inclusive.
            :param windowEnd: End position of the window on the reference sequence. If the coordinate system
        is 0-based then end is exclusive and does not include the last position. If
        the coordinate system is 1-base, then end is inclusive and includes the last
        position.
        """
        super().__init__(
            resourceType="MolecularSequenceReferenceSeq",
            id_=id_,
            meta=meta,
            extension=extension,
            chromosome=chromosome,
            genomeBuild=genomeBuild,
            orientation=orientation,
            referenceSeqId=referenceSeqId,
            referenceSeqPointer=referenceSeqPointer,
            referenceSeqString=referenceSeqString,
            strand=strand,
            windowStart=windowStart,
            windowEnd=windowEnd,
        )