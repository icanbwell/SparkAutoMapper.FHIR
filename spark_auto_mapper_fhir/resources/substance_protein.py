from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.substanceprotein import SubstanceProteinSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.integer import FhirInteger
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.backbone_elements.substance_protein_subunit import (
        SubstanceProteinSubunit,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceProtein(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        sequenceType: Optional[CodeableConcept] = None,
        numberOfSubunits: Optional[FhirInteger] = None,
        disulfideLinkage: Optional[FhirList[FhirString]] = None,
        subunit: Optional[FhirList[SubstanceProteinSubunit]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param sequenceType: The SubstanceProtein descriptive elements will only be used when a complete or
        partial amino acid sequence is available or derivable from a nucleic acid
        sequence.
            :param numberOfSubunits: Number of linear sequences of amino acids linked through peptide bonds. The
        number of subunits constituting the SubstanceProtein shall be described. It is
        possible that the number of subunits can be variable.
            :param disulfideLinkage: The disulphide bond between two cysteine residues either on the same subunit
        or on two different subunits shall be described. The position of the disulfide
        bonds in the SubstanceProtein shall be listed in increasing order of subunit
        number and position within subunit followed by the abbreviation of the amino
        acids involved. The disulfide linkage positions shall actually contain the
        amino acid Cysteine at the respective positions.
            :param subunit: This subclause refers to the description of each subunit constituting the
        SubstanceProtein. A subunit is a linear sequence of amino acids linked through
        peptide bonds. The Subunit information shall be provided when the finished
        SubstanceProtein is a complex of multiple sequences; subunits are not used to
        delineate domains within a single sequence. Subunits are listed in order of
        decreasing length; sequences of the same length will be ordered by decreasing
        molecular weight; subunits that have identical sequences will be repeated
        multiple times.
        """
        super().__init__(
            resourceType="SubstanceProtein",
            id_=id_,
            meta=meta,
            extension=extension,
            sequenceType=sequenceType,
            numberOfSubunits=numberOfSubunits,
            disulfideLinkage=disulfideLinkage,
            subunit=subunit,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return SubstanceProteinSchema.get_schema(include_extension=include_extension)